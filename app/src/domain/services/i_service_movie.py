from abc import ABC, abstractmethod
from app.src.domain.models.model_movie import ModelMovie

class IServiceMovie(ABC):

    @abstractmethod
    async def getAll(self, page: int, limit: int) -> list[ModelMovie]:
        pass

    @abstractmethod
    async def getById(self, id: str) -> ModelMovie:
        pass

    @abstractmethod
    async def getByCategory(self, category: str, page: int, limit: int) -> list[ModelMovie]:
        pass

    @abstractmethod
    async def create(self, movie: ModelMovie) -> ModelMovie:
        pass

    @abstractmethod
    async def updateById(self, movie: ModelMovie, id: str) -> ModelMovie:
        pass

    @abstractmethod
    async def deleteById(self, id: str) -> str:
        pass