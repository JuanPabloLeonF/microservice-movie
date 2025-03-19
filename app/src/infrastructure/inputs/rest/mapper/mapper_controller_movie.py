from app.src.application.dto.request_movie import MovieRequest
from app.src.infrastructure.inputs.rest.dto.movie_request_controller import MovieRequestForm

class IMapperControllerMovie:

    @staticmethod
    def mapperMovieRequestFormToMovieRequest(movieRequestForm: MovieRequestForm) -> MovieRequest:
        return MovieRequest(
            title=movieRequestForm.title,
            description=movieRequestForm.description,
            dateCreated=movieRequestForm.dateCreation,
            category=movieRequestForm.category,
            imgFile=movieRequestForm.imgFile,
            videoFile=movieRequestForm.videoFile
        )