from backend.models.member import Member
from backend.utils.repository import SQLAlchemyRepository


class MemberRepo(SQLAlchemyRepository):
    model = Member
