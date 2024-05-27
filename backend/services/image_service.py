from backend.repositories.image_repository import ImageRepo


class ImageService:

    def __init__(self, repo: ImageRepo):
        self.repo: ImageRepo = repo()

    async def upload_image(self, image):
        filename = image.filename
        filepath = 'static/' + filename
        with open(filepath, 'wb') as f:
            f.write(image.file.read())

        image_id = await self.repo.add_one({"name": filename, "path": filepath})
        return image_id
