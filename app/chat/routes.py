from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.llm import get_ai_response
from app.db.database import get_db
from app.chat.models import ChatMessage
from app.projects.models import Project
from app.core.dependencies import get_current_user
from app.users.models import User
from app.prompts.models import Prompt

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@router.post("/{project_id}")
def chat_with_bot(
    project_id: int,
    message: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    project = db.query(Project).filter(
        Project.id == project_id,
        Project.owner_id == current_user.id
    ).first()

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found or unauthorized"
        )

    # Save user message
    user_msg = ChatMessage(
        project_id=project_id,
        role="user",
        content=message
    )

    db.add(user_msg)
    db.commit()

    
    prompt = db.query(Prompt).filter(
        Prompt.project_id == project_id
    ).first()

    system_prompt = prompt.content if prompt else None

    bot_reply = get_ai_response(message, system_prompt)


    # Save bot message
    bot_msg = ChatMessage(
        project_id=project_id,
        role="assistant",
        content=bot_reply
    )

    db.add(bot_msg)
    db.commit()

    return {
        "project": project.name,
        "user_message": message,
        "bot_reply": bot_reply
    }
