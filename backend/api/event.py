from typing import Annotated

from fastapi import APIRouter, Depends

from backend.api.deps import event_service
from backend.services.event_service import EventService

router = APIRouter(
    prefix="/event",
    tags=["event"],
)


@router.get("/")
async def get_all(
        service: Annotated[EventService, Depends(event_service)],
):
    res = await service.get_list()
    return res


@router.get("/{id}")
async def get_by_id(
        id: int,
        service: Annotated[EventService, Depends(event_service)],
):
    res = await service.get_by_id(id)
    return res
