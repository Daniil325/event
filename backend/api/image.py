from typing import Annotated

from fastapi import APIRouter, Depends, UploadFile, File

from backend.api.deps import image_service
from backend.services.image_service import ImageService

router = APIRouter(
    prefix="/images",
    tags=["images"],
)


@router.post("/")
async def create_image(
        service: Annotated[ImageService, Depends(image_service)],
        image: UploadFile = File(...),
):
    obj = await service.upload_image(image)
    return obj
