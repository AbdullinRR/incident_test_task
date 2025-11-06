from sqlalchemy.ext.asyncio import AsyncSession

from core.schemas.incident import IncidentCreate, IncidentUpdate
from db.incident import IncidentRepository


class IncidentService:
    def __init__(self, db: AsyncSession):
        self.repo = IncidentRepository(db)

    async def create_incident(self, data: IncidentCreate):
        return await self.repo.create(data)

    async def get_incidents(self, status: str | None = None):
        if status:
            return await self.repo.get_by_status(status)
        return await self.repo.get_all()

    async def update_status(self, incident_id: int, data: IncidentUpdate):
        return await self.repo.update_status(incident_id, data.status)