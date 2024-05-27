from backend.repositories.member_repository import MemberRepo


class MemberService:

    def __init__(self, repo: MemberRepo):
        self.repo: MemberRepo = repo()

    async def add_member(self, obj):
        obj_dict = obj.model_dump()
        obj_dict_id = await self.repo.add_one(obj_dict)
        return obj_dict_id
