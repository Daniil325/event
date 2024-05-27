from backend.utils.repository import SQLAlchemyRepository
from backend.models.member_in_event import MemberInEvent


class MemberInEventRepo(SQLAlchemyRepository):
    model = MemberInEvent
