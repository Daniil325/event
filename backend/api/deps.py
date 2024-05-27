from backend.repositories.event_repository import EventRepo
from backend.repositories.image_repository import ImageRepo
from backend.repositories.member_in_event_repo import MemberInEventRepo
from backend.repositories.member_repository import MemberRepo
from backend.services.event_service import EventService
from backend.services.image_service import ImageService
from backend.services.member_in_event import MemberInEventService
from backend.services.member_service import MemberService


def image_service():
    return ImageService(ImageRepo)


def event_service():
    return EventService(EventRepo)


def member_service():
    return MemberService(MemberRepo)


def member_in_event_service():
    return MemberInEventService(MemberInEventRepo)
