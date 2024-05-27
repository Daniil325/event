from fastapi import FastAPI
from sqladmin import Admin
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from backend.api.image import router as image_router
from backend.api.event import router as event_router
from backend.api.member import router as member_router
from backend.api.member_in_event import router as member_in_event_router
from backend.db.db import engine
from backend.admin.view import *

app = FastAPI()

admin = Admin(app, engine)

admin.add_view(EventAdmin)
admin.add_view(EventTypeAdmin)
admin.add_view(ImageAdmin)
admin.add_view(MemberAdmin)
admin.add_view(MemberInEventAdmin)

app.include_router(image_router)
app.include_router(event_router)
app.include_router(member_router)
app.include_router(member_in_event_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
