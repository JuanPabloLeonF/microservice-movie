from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from app.configuration.exceptions_personalities import IntegrityErrorDatabase
from app.src.infrastructure.outputs.mysql.repositories.i_repository_movie import IRepositoryMovie
from app.src.infrastructure.outputs.mysql.settings.database_config import DatabaseConfiguration
from app.src.infrastructure.outputs.mysql.entities.movie_entity import MovieEntity
from app.src.application.utils.utils_file_application import UtilsFilesApplication

class ImplementationMovieRepository(IRepositoryMovie):

    async def getAll(self, page: int, limit: int) -> list[MovieEntity]:
        async with DatabaseConfiguration.getSession() as session:
            result = await session.execute(
                select(MovieEntity).
                limit(limit).
                offset((page - 1) * limit)
            )
            return result.scalars().all()

    async def getById(self, id: str) -> MovieEntity:
        async with DatabaseConfiguration.getSession() as session:
            result = await session.get(MovieEntity, id)
            if not result:
                raise ValueError(f"Movie not found by the id: {id}")
            return result


    async def getByCategory(self, category: str, page: int, limit: int) -> list[MovieEntity]:
        async with DatabaseConfiguration.getSession() as session:
            result = await session.execute(
                select(MovieEntity).
                where(MovieEntity.category.contains(category)).
                limit(limit).
                offset((page - 1) * limit)
            )
            return result.scalars().all()

    async def create(self, movie: MovieEntity) -> MovieEntity:
        async with DatabaseConfiguration.getSession() as session:
            try:
                session.add(movie)
                await session.commit()
                await session.refresh(movie)
                return movie
            except IntegrityError as error:
                await session.rollback()
                raise IntegrityErrorDatabase(str(error))
            except SQLAlchemyError as error:
                await session.rollback()
                raise RuntimeError(str(error))

    async def updateById(self, movie: MovieEntity, id: str) -> MovieEntity:
        async with DatabaseConfiguration.getSession() as session:
            try:
                movieFound = await session.get(MovieEntity, id)
                if not movieFound:
                    UtilsFilesApplication.deletedFile(filePath=movie.imgUrlCover)
                    UtilsFilesApplication.deletedFile(filePath=movie.videoUrl)
                    raise ValueError(f"Movie not found by the id: {id}")

                UtilsFilesApplication.deletedFile(filePath=movieFound.imgUrlCover)
                UtilsFilesApplication.deletedFile(filePath=movieFound.videoUrl)

                movieFound.title = movie.getTitle()
                movieFound.description = movie.getDescription()
                movieFound.dateCreated = movie.getDateCreated()
                movieFound.category = movie.getCategory()
                movieFound.imgUrlCover = movie.getImgUrlCover()
                movieFound.videoUrl = movie.getVideoUrl()
                await session.commit()
                await session.refresh(movieFound)
                return movieFound
            except IntegrityError as error:
                await session.rollback()
                raise IntegrityErrorDatabase(str(error))
            except SQLAlchemyError as error:
                await session.rollback()
                raise RuntimeError(str(error))


    async def deleteById(self, id: str) -> str:
        async with DatabaseConfiguration.getSession() as session:
            try:
                movieFound = await session.get(MovieEntity, id)
                if not movieFound:
                    raise ValueError(f"Movie not found by id: {id}")
                UtilsFilesApplication.deletedFile(filePath=movieFound.imgUrlCover)
                UtilsFilesApplication.deletedFile(filePath=movieFound.videoUrl)
                await session.delete(movieFound)
                await session.commit()
                return f"Movie deleted successfully by the id: {id}"
            except IntegrityError as error:
                await session.rollback()
                raise IntegrityErrorDatabase(str(error))
            except SQLAlchemyError as error:
                await session.rollback()
                raise RuntimeError(str(error))