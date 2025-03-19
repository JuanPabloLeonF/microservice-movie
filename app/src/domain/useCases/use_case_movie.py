from app.src.domain.services.i_service_movie import IServiceMovie
from app.src.domain.persistence.i_persistence_movie import IPersistenceMovie
from app.src.domain.models.model_movie import ModelMovie

class UseCaseMovie(IServiceMovie):

    def __init__(self, iPersistenceMovie: IPersistenceMovie):
        self.iPersistenceMovie: IPersistenceMovie = iPersistenceMovie

    async def getAll(self, page: int, limit: int) -> list[ModelMovie]:
        return await self.iPersistenceMovie.getAll(page=page, limit=limit)

    async def getById(self, id: str) -> ModelMovie:
        return await self.iPersistenceMovie.getById(id)

    async def getByCategory(self, category: str, page: int, limit: int) -> list[ModelMovie]:
        return await self.iPersistenceMovie.getByCategory(category=category, page=page, limit=limit)

    async def create(self, movie: ModelMovie) -> ModelMovie:
        return await self.iPersistenceMovie.create(movie)

    async def updateById(self, movie: ModelMovie, id: str) -> ModelMovie:
        return await self.iPersistenceMovie.updateById(movie, id)

    async def deleteById(self, id: str) -> str:
        return await self.iPersistenceMovie.deleteById(id)