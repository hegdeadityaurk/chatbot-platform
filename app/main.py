from fastapi import FastAPI
from app.db.database import engine
from app.users.models import User
from app.db.database import Base
from app.projects.models import Project
from app.chat.models import ChatMessage
from app.auth.routes import router as auth_router
from app.projects.routes import router as project_router
from app.chat.routes import router as chat_router
from app.prompts.models import Prompt
from app.prompts.routes import router as prompt_router
app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(auth_router)
app.include_router(project_router)
app.include_router(chat_router)
app.include_router(prompt_router)

