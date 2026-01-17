from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.prompts.models import Prompt
from app.projects.models import Project
from app.core.dependencies import get_current_user
from app.users.models import User

router = APIRouter(
    prefix="/prompts",
    tags=["Prompts"]
)

@router.post("/{project_id}")
def create_prompt(
    project_id: int,
    content: str,
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

    existing_prompt = db.query(Prompt).filter(
        Prompt.project_id == project_id
    ).first()

    if existing_prompt:
        raise HTTPException(
            status_code=400,
            detail="Prompt already exists for this project"
        )

    new_prompt = Prompt(
        project_id=project_id,
        content=content
    )

    db.add(new_prompt)
    db.commit()
    db.refresh(new_prompt)

    return {
        "message": "Prompt created successfully",
        "prompt": new_prompt.content
    }

@router.get("/{project_id}")
def get_prompt(
    project_id: int,
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

    prompt = db.query(Prompt).filter(
        Prompt.project_id == project_id
    ).first()

    if not prompt:
        return {"prompt": None}

    return {"prompt": prompt.content}

@router.put("/{project_id}")
def update_prompt(
    project_id: int,
    content: str,
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

    prompt = db.query(Prompt).filter(
        Prompt.project_id == project_id
    ).first()

    if not prompt:
        raise HTTPException(
            status_code=404,
            detail="Prompt not found"
        )

    prompt.content = content
    db.commit()

    return {
        "message": "Prompt updated successfully",
        "prompt": prompt.content
    }
