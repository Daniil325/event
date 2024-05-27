from typing import Annotated

from fastapi import APIRouter, Depends

from backend.api.deps import member_in_event_service
from backend.schemas.member_in_event_schema import MemberInEventSchema
from backend.services.member_in_event import MemberInEventService

router = APIRouter(
    prefix="/member_in_event",
    tags=["member_in_event"],
)


@router.post("/")
async def post_member(
        service: Annotated[MemberInEventService, Depends(member_in_event_service)],
        member: MemberInEventSchema
):
    member_id = await service.add_member(member)
    return {"member_in_event_id": member_id}
