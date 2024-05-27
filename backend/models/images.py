from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import mapped_column

from backend.db.db import Base


class Image(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False)
    path = mapped_column(String, nullable=False)

    def __init__(self, name, path):
        self.name = name
        self.path = path
