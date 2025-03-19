from app.src.infrastructure.outputs.mysql.entities.movie_entity import MovieEntity
from app.src.infrastructure.outputs.mysql.repositories.i_repository_movie import IRepositoryMovie
from app.src.infrastructure.outputs.mysql.mappers.i_mapper_entity_movie import IMapperEntityMovie
from app.src.domain.models.model_movie import ModelMovie
from app.src.domain.persistence.i_persistence_movie import IPersistenceMovie

class AdapterMovie(IPersistenceMovie):

    def __init__(self, iRepositoryMovie: IRepositoryMovie, iMapperEntityMovie: IMapperEntityMovie):
        self.iRepositoryMovie: IRepositoryMovie = iRepositoryMovie
        self.iMapperEntityMovie: IMapperEntityMovie = iMapperEntityMovie

    async def getAll(self, page: int, limit: int) -> list[ModelMovie]:
        listMovieEntity: list[MovieEntity] = await self.iRepositoryMovie.getAll(page=page, limit=limit)
        return self.iMapperEntityMovie.mapperListMovieEntityToListMovieModel(listMovieEntity)

    async def getById(self, id: str) -> ModelMovie:
        movieEntity: MovieEntity = await self.iRepositoryMovie.getById(id)
        return self.iMapperEntityMovie.mapperMovieEntityToModelMovie(movieEntity)

    async def getByCategory(self, category: str, page: int, limit: int) -> list[ModelMovie]:
        listMovieEntity: list[MovieEntity] = await self.iRepositoryMovie.getByCategory(category=category, page=page, limit=limit)
        return self.iMapperEntityMovie.mapperListMovieEntityToListMovieModel(listMovieEntity)

    async def create(self, movie: ModelMovie) -> ModelMovie:
        movieEntity: MovieEntity = self.iMapperEntityMovie.mapperMovieModelToMovieEntity(movie)
        movieEntity = await self.iRepositoryMovie.create(movieEntity)
        return self.iMapperEntityMovie.mapperMovieEntityToModelMovie(movieEntity)

    async def updateById(self, movie: ModelMovie, id: str) -> ModelMovie:
        movieEntity: MovieEntity = self.iMapperEntityMovie.mapperMovieModelToMovieEntity(movie)
        movieEntity = await self.iRepositoryMovie.updateById(movieEntity, id)
        return self.iMapperEntityMovie.mapperMovieEntityToModelMovie(movieEntity)

    async def deleteById(self, id: str) -> str:
        return await self.iRepositoryMovie.deleteById(id)