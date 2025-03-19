from abc import ABC, abstractmethod
from app.src.application.dto.movie_response import MovieResponse
from app.src.application.dto.request_movie import MovieRequest

class IHandlerMovie(ABC):

    @abstractmethod
    async def getAll(self, page: int, limit: int) -> list[MovieResponse]:
        pass

    @abstractmethod
    async def getById(self, id: str) -> MovieResponse:
        pass

    @abstractmethod
    async def getByCategory(self, category: str, page: int, limit: int) -> list[MovieResponse]:
        pass

    @abstractmethod
    async def create(self, movie: MovieRequest) -> MovieResponse:
        pass

    @abstractmethod
    async def updateById(self, movie: MovieRequest, id: str) -> MovieResponse:
        pass

    @abstractmethod
    async def deleteById(self, id: str) -> str:
        pass