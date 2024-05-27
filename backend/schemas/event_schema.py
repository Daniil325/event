from pydantic import BaseModel


class EventSchema(BaseModel):
    id: int
    name: str
    description: str
    file: str
    event_type: str