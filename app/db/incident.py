from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from core.models.incident import Incident
from core.schemas.incident import IncidentCreate


class IncidentRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, data: IncidentCreate):
        incident = Incident(**data.dict())
        self.db.add(incident)
        await self.db.commit()
        await self.db.refresh(incident)
        return incident

    async def get_all(self):
        result = await self.db.execute(select(Incident))
        return result.scalars().all()

    async def get_by_status(self, status: str):
        result = await self.db.execute(select(Incident).where(Incident.status == status))
        return result.scalars().all()

    async def update_status(self, incident_id: int, status: str):
        result = await self.db.execute(select(Incident).where(Incident.id == incident_id))
        incident = result.scalar_one_or_none()
        if not incident:
            return None
        incident.status = status
        await self.db.commit()
        await self.db.refresh(incident)
        return incident