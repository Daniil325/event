from sqladmin import ModelView

from backend.models.event import Event
from backend.models.member_in_event import MemberInEvent
from backend.models.type_event import EventType
from backend.models.images import Image
from backend.models.member import Member


class EventAdmin(ModelView, model=Event):
    column_list = '__all__'
    name = 'Мероприятие'
    name_plural = 'Мероприятия'


class EventTypeAdmin(ModelView, model=EventType):
    column_list = '__all__'
    name = 'Тип мероприятия'
    name_plural = 'Типы мероприятий'


class ImageAdmin(ModelView, model=Image):
    column_list = '__all__'
    name = 'Изображение'
    name_plural = 'Изображения'


class MemberAdmin(ModelView, model=Member):
    column_list = '__all__'
    name = 'Участник'
    name_plural = 'Участники'


class MemberInEventAdmin(ModelView, model=MemberInEvent):
    column_list = '__all__'
    name = 'Участник в мероприятии'
    name_plural = 'Участники в мероприятиях'
