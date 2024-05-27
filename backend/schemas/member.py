from pydantic import BaseModel


class MemberSchema(BaseModel):
    fio: str
    phone: str
    email: str
