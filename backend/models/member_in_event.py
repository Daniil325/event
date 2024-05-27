from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, mapped_column

from backend.db.db import Base
from backend.models.event import Event
from backend.models.member import Member


class MemberInEvent(Base):
    __tablename__ = 'member_in_event'

    id = Column(Integer, primary_key=True)
    event_id = mapped_column(Integer, ForeignKey(Event.id))
    member_id = mapped_column(Integer, ForeignKey(Member.id))

    event = relationship(
        Event, foreign_keys=[event_id], lazy='joined'
    )
    member = relationship(
        Member, foreign_keys=[member_id], lazy='joined'
    )
