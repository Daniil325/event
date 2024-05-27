from backend.repositories.event_repository import EventRepo
import base64


class EventService:
    def __init__(self, event_repo: EventRepo):
        self.repo: EventRepo = event_repo()

    async def get_list(self):
        res = await self.repo.find_all()
        for i in res:

            with open(i.file, "rb") as image_file:
                i.file = "data:image/png;base64,"
                i.file += base64.b64encode(image_file.read()).decode('utf-8')

        return res

    async def get_by_id(self, event_id):
        res = await self.repo.get_by_id(event_id)
        for i in res:

            with open(i.file, "rb") as image_file:
                i.file = "data:image/png;base64,"
                i.file += base64.b64encode(image_file.read()).decode('utf-8')

        return res
