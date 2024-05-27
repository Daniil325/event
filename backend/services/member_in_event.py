from backend.repositories.member_in_event_repo import MemberInEventRepo


class MemberInEventService:

    def __init__(self, repo: MemberInEventRepo):
        self.repo: MemberInEventRepo = repo()

    async def add_member(self, obj):
        obj_dict = obj.model_dump()
        obj_dict_id = await self.repo.add_one(obj_dict)
        return obj_dict_id
