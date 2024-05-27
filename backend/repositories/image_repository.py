from backend.utils.repository import SQLAlchemyRepository
from backend.models.images import Image


class ImageRepo(SQLAlchemyRepository):
    model = Image
