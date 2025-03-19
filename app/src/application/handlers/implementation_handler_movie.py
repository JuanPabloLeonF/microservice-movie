from app.src.application.handlers.i_handler_movie import IHandlerMovie
from app.src.domain.models.model_movie import ModelMovie
from app.src.domain.services.i_service_movie import IServiceMovie
from app.src.application.dto.request_movie import MovieRequest
from app.src.application.dto.movie_response import MovieResponse
from app.src.application.mappers.i_mapper_handler import IMapperHandler
from app.src.application.utils.utils_file_application import UtilsFilesApplication

class ImplementationHandlerMovie(IHandlerMovie):

    def __init__(self, iMapperHandler: IMapperHandler, iServiceMovie: IServiceMovie):
        self.iMapperHandler: IMapperHandler = iMapperHandler
        self.iServiceMovie: IServiceMovie = iServiceMovie

    async def getAll(self, page: int, limit: int) -> list[MovieResponse]:
        responseListModelMovie: list[ModelMovie] = await self.iServiceMovie.getAll(page=page, limit=limit)
        response: list[MovieResponse] = self.iMapperHandler.mapperListModelMovieToListMovieResponse(listModel=responseListModelMovie)
        return [data.getJSON() for data in response]

    async def getById(self, id: str) -> MovieResponse:
        movieResponse: MovieResponse = self.iMapperHandler.mapperModelMovieToMovieResponse(model=await self.iServiceMovie.getById(id=id))
        return movieResponse.getJSON()

    async def getByCategory(self, category: str, page: int, limit: int) -> list[MovieResponse]:
        responseListModelMovie: list[ModelMovie] = await self.iServiceMovie.getByCategory(category=category, page=page, limit=limit)
        response: list[MovieResponse] = self.iMapperHandler.mapperListModelMovieToListMovieResponse(listModel=responseListModelMovie)
        return [data.getJSON() for data in response]

    async def create(self, movie: MovieRequest) -> MovieResponse:
        imgUrl: str = UtilsFilesApplication.saveFile(file=movie.getImgFile(), folderName="files/images")
        videoUrl: str = UtilsFilesApplication.saveFile(file=movie.getVideoFile(), folderName="files/videos")
        movie: ModelMovie = self.iMapperHandler.mapperMovieRequestToModelMovie(request=movie, imgUrl=imgUrl, videoUrl=videoUrl)
        movieResponse: MovieResponse = self.iMapperHandler.mapperModelMovieToMovieResponse(model=await self.iServiceMovie.create(movie=movie))
        return movieResponse.getJSON()

    async def updateById(self, movie: MovieRequest, id: str) -> MovieResponse:
        imgUrl: str = UtilsFilesApplication.saveFile(file=movie.getImgFile(), folderName="files/images")
        videoUrl: str = UtilsFilesApplication.saveFile(file=movie.getVideoFile(), folderName="files/videos")
        movie: ModelMovie = self.iMapperHandler.mapperMovieRequestToModelMovie(request=movie, imgUrl=imgUrl, videoUrl=videoUrl)
        movieResponse: MovieResponse = self.iMapperHandler.mapperModelMovieToMovieResponse(model=await self.iServiceMovie.updateById(movie=movie, id=id))
        return movieResponse.getJSON()

    async def deleteById(self, id: str) -> str:
        return await self.iServiceMovie.deleteById(id=id)