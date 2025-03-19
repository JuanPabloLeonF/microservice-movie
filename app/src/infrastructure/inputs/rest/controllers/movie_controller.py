import injector
from fastapi import APIRouter,status, Depends
from fastapi.responses import JSONResponse

from app.src.application.dto.movie_response import MovieResponse
from app.src.application.dto.request_movie import MovieRequest
from app.src.application.handlers.i_handler_movie import IHandlerMovie
from app.configuration.module_injector_user import ModuleInjectorMovie
from app.src.infrastructure.inputs.rest.dto.movie_request_controller import MovieRequestForm
from app.src.infrastructure.inputs.rest.mapper.mapper_controller_movie import IMapperControllerMovie

movieRouter: APIRouter = APIRouter(prefix="/movie")
iHandler: IHandlerMovie = injector.Injector([ModuleInjectorMovie()]).get(IHandlerMovie)
iMapperControllerMovie: IMapperControllerMovie = IMapperControllerMovie()

class MovieController:

    @staticmethod
    @movieRouter.get("/all/{page}/{limit}", status_code=200)
    async def getAll(page: int, limit: int):
        response: list[MovieResponse] = await iHandler.getAll(page=page, limit=limit)
        return JSONResponse(content=response, status_code=status.HTTP_200_OK)

    @staticmethod
    @movieRouter.get("/getById/{id}", status_code=200)
    async def getById(id: str):
        response: MovieResponse = await iHandler.getById(id=id)
        return JSONResponse(content=response, status_code=status.HTTP_200_OK)

    @staticmethod
    @movieRouter.get("/getByCategory/{category}/{page}/{limit}", status_code=200)
    async def getByCategory(category: str, page: int, limit: int):
        response: list[MovieResponse] = await iHandler.getByCategory(category=category, page=page, limit=limit)
        return JSONResponse(content=response, status_code=status.HTTP_200_OK)

    @staticmethod
    @movieRouter.post("/create", status_code=201)
    async def create(request: MovieRequestForm = Depends(MovieRequestForm)):
        movieRequest: MovieRequest = iMapperControllerMovie.mapperMovieRequestFormToMovieRequest(movieRequestForm=request)
        response: MovieResponse = await iHandler.create(movie=movieRequest)
        return JSONResponse(content=response, status_code=status.HTTP_201_CREATED)

    @staticmethod
    @movieRouter.put("/updateById/{id}", status_code=200)
    async def updateById(id: str, request: MovieRequestForm = Depends(MovieRequestForm)):
        movieRequest: MovieRequest = iMapperControllerMovie.mapperMovieRequestFormToMovieRequest(movieRequestForm=request)
        response: MovieResponse = await iHandler.updateById(movie=movieRequest, id=id)
        return JSONResponse(content=response, status_code=status.HTTP_200_OK)

    @staticmethod
    @movieRouter.delete("/deleteById/{id}", status_code=200)
    async def deleteById(id: str):
        response: str = await iHandler.deleteById(id=id)
        return JSONResponse(content=response, status_code=status.HTTP_200_OK)