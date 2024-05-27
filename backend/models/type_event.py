from sqlalchemy import Column, Integer, String

from backend.db.db import Base


class EventType(Base):
    __tablename__ = 'type_event'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __str__(self):
        return self.name
