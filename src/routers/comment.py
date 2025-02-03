from fastapi import APIRouter, Path, Query, HTTPException, Depends
from starlette import status
from sqlalchemy.orm import Session
from typing import Annotated

from cruds import comment as comment_cruds, auth as auth_cruds
from schemas import CommentCreate, CommentUpdate, CommentResponse, DecodedToken
from database import get_db

# 依存性の注入
DbDependency = Annotated[Session, Depends(get_db)]

# 認証機能対応
UserDependency = Annotated[DecodedToken, Depends(auth_cruds.get_current_user)]

router = APIRouter(prefix="/comment", tags=["comment"])


@router.get("", response_model=list[CommentResponse], status_code=status.HTTP_200_OK)
async def find_all(db: DbDependency):
    return comment_cruds.find_all_comments(db)


@router.get("/{id}", response_model=CommentResponse, status_code=status.HTTP_200_OK)
async def find_comment_by_id(
    db: DbDependency, user: UserDependency, id: int = Path(gt=0)
):
    found_comment = comment_cruds.find_comment_by_id(db, id, user.user_id)
    if not found_comment:
        raise HTTPException(status_code=404, detail="Item not found")
    return found_comment


@router.get("/", response_model=list[CommentResponse], status_code=status.HTTP_200_OK)
async def find_comments_by_content(
    db: DbDependency, content: str = Query(min_length=2, max_length=20)
):
    return comment_cruds.find_comments_by_content(db, content)


@router.post("", response_model=CommentResponse, status_code=status.HTTP_201_CREATED)
async def create(db: DbDependency, user: UserDependency, comment_create: CommentCreate):
    return comment_cruds.create_comment(db, comment_create, user.user_id)


@router.put("/{id}", response_model=CommentResponse, status_code=status.HTTP_200_OK)
async def update(
    db: DbDependency,
    user: UserDependency,
    comment_update: CommentUpdate,
    id: int = Path(gt=0),
):
    updated_comment = comment_cruds.update_comment(db, id, comment_update, user.user_id)
    if not updated_comment:
        raise HTTPException(status_code=404, detail="Item not updated")
    return updated_comment


@router.delete("/{id}", response_model=CommentResponse, status_code=status.HTTP_200_OK)
async def delete(
    db: DbDependency,
    user: UserDependency,
    id: int = Path(gt=0),
):
    deleted_comment = comment_cruds.delete_comment(db, id, user.user_id)
    if not deleted_comment:
        raise HTTPException(status_code=404, detail="Item not deleted")
    return deleted_comment
