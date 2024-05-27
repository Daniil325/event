from fastapi_storages.integrations.sqlalchemy import FileType
from sqlalchemy import Column, Integer, ForeignKey, String, Date
from sqlalchemy.orm import mapped_column, relationship
from fastapi_storages import FileSystemStorage
from backend.db.db import Base
from backend.models.type_event import EventType

storage = FileSystemStorage(path="static")


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    dat = Column(Date)
    event_type_id = mapped_column(ForeignKey(EventType.id))
    file = Column(FileType(storage=storage))

    event_type = relationship(
        EventType, foreign_keys=[event_type_id], lazy='joined'
    )

    def __str__(self):
        return self.name
