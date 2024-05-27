from pydantic import BaseModel


class MemberInEventSchema(BaseModel):
    event_id: int
    member_id: int
