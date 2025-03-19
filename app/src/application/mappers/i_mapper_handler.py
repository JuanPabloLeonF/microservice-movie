from app.src.domain.models.model_movie import ModelMovie
from app.src.application.dto.request_movie import MovieRequest
from app.src.application.dto.movie_response import MovieResponse

class IMapperHandler:

    @staticmethod
    def mapperMovieRequestToModelMovie(request: MovieRequest, imgUrl: str, videoUrl: str) -> ModelMovie:
        return ModelMovie(
            id = "",
            title = request.getTitle(),
            description = request.getDescription(),
            dateCreated = request.getDateCreated(),
            category = request.getCategory(),
            imgUrlCover =imgUrl,
            videoUrl = videoUrl
        )

    @staticmethod
    def mapperModelMovieToMovieResponse(model: ModelMovie) -> MovieResponse:
        return MovieResponse(
            id = model.getId(),
            title = model.getTitle(),
            description = model.getDescription(),
            dateCreated = model.getDateCreated(),
            category = model.getCategory(),
            imgUrlCover = model.getImgUrlCover(),
            videoUrl = model.getVideoUrl()
        )

    @staticmethod
    def mapperListModelMovieToListMovieResponse(listModel: list[ModelMovie]) -> list[MovieResponse]:
        return [IMapperHandler.mapperModelMovieToMovieResponse(model) for model in listModel]