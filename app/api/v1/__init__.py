from fastapi import APIRouter

from .incident import router as incident_router


router = APIRouter(prefix="/v1")
router.include_router(incident_router)