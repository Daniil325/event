from fastapi import File, UploadFile
from pydantic import BaseModel


class ImageUploadSchema(BaseModel):
    name: str
    select_as_title: bool = False
    image: UploadFile = File(...)
