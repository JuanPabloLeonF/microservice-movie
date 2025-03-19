from app.src.domain.models.model_movie import ModelMovie
from app.src.infrastructure.outputs.mysql.entities.movie_entity import MovieEntity

class IMapperEntityMovie:

    @staticmethod
    def mapperMovieEntityToModelMovie(movieEntity: MovieEntity) -> ModelMovie:
        return ModelMovie(
            id=movieEntity.getId(),
            title=movieEntity.getTitle(),
            description=movieEntity.getDescription(),
            dateCreated=movieEntity.getDateCreated(),
            category=movieEntity.getCategory(),
            imgUrlCover=movieEntity.getImgUrlCover(),
            videoUrl=movieEntity.getVideoUrl()
        )

    @staticmethod
    def mapperMovieModelToMovieEntity(movieModel: ModelMovie) -> MovieEntity:
        return MovieEntity(
            title=movieModel.getTitle(),
            description=movieModel.getDescription(),
            dateCreated=movieModel.getDateCreated(),
            category=movieModel.getCategory(),
            imgUrlCover=movieModel.getImgUrlCover(),
            videoUrl=movieModel.getVideoUrl()
        )

    @staticmethod
    def mapperListMovieEntityToListMovieModel(listMovieEntity: list[MovieEntity]) -> list[ModelMovie]:
        return [IMapperEntityMovie.mapperMovieEntityToModelMovie(movieEntity) for movieEntity in listMovieEntity]