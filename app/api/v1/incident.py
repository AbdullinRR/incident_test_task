from typing import List

from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from core.database import get_db
from core.schemas import IncidentResponse, IncidentCreate, IncidentUpdate
from services.incident import IncidentService


router = APIRouter(prefix="/incident", tags=["Incident"])

@router.post("/", response_model=IncidentResponse, summary="создать новый инцидент")
async def create_incident(incident_data: IncidentCreate, db = Depends(get_db)):
    return await IncidentService(db).create_incident(incident_data)

@router.get("/", response_model=List[IncidentResponse], summary="получить все инциденты (фильтр по статусу")
async def get_incidents(status: str | None = None, db = Depends(get_db)):
    return await IncidentService(db).get_incidents(status=status)

@router.patch("/{incident_id}", response_model=IncidentResponse, summary="обновить статус инцидента")
async def update_status(incident_id: int, update_data: IncidentUpdate, db = Depends(get_db)):
    updated = await IncidentService(db).update_status(incident_id, update_data)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incident not found")
    return updated