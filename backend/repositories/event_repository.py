from backend.models.event import Event
from backend.utils.repository import SQLAlchemyRepository


class EventRepo(SQLAlchemyRepository):
    model = Event
