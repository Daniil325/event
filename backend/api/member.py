from typing import Annotated

from fastapi import APIRouter, Depends

from backend.api.deps import member_service
from backend.schemas.member import MemberSchema
from backend.services.member_service import MemberService

router = APIRouter(
    prefix="/member",
    tags=["member"],
)


@router.post("/")
async def post_member(
        service: Annotated[MemberService, Depends(member_service)],
        member: MemberSchema
):
    member_id = await service.add_member(member)
    return {"member_id": member_id}
