from sqlalchemy import Column, Integer, String

from backend.db.db import Base


class Member(Base):
    __tablename__ = 'member'

    id = Column(Integer, primary_key=True)
    fio = Column(String)
    phone = Column(String)
    email = Column(String)

    def __str__(self):
        return self.fio
