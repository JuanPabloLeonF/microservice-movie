from abc import ABC, abstractmethod
from app.src.infrastructure.outputs.mysql.entities.movie_entity import MovieEntity

class IRepositoryMovie(ABC):

    @abstractmethod
    async def getAll(self, page: int, limit: int) -> list[MovieEntity]:
        pass

    @abstractmethod
    async def getById(self, id: str) -> MovieEntity:
        pass

    @abstractmethod
    async def getByCategory(self, category: str, page: int, limit: int) -> list[MovieEntity]:
        pass

    @abstractmethod
    async def create(self, movie: MovieEntity) -> MovieEntity:
        pass

    @abstractmethod
    async def updateById(self, movie: MovieEntity, id: str) -> MovieEntity:
        pass

    @abstractmethod
    async def deleteById(self, id: str) -> str:
        pass