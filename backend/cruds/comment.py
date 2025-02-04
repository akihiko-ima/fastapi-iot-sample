from sqlalchemy.orm import Session
from typing import Optional

from models import Comment
from schemas import CommentCreate, CommentUpdate


def find_all_comments(db: Session):
    return db.query(Comment).all()


def find_comment_by_id(db: Session, id: int, user_id: int):
    return (
        db.query(Comment)
        .filter(Comment.id == id)
        .filter(Comment.user_id == user_id)
        .first()
    )


def find_comments_by_content(db: Session, content: str):
    return db.query(Comment).filter(Comment.content.like(f"%{content}%")).all()


def create_comment(db: Session, comment_create: CommentCreate, user_id: int):
    new_comment = Comment(**comment_create.model_dump(), user_id=user_id)
    db.add(new_comment)
    db.commit()
    return new_comment


def update_comment(db: Session, id: int, comment_update: CommentUpdate, user_id: int):
    comment = find_comment_by_id(db, id, user_id)
    if comment is None:
        return None

    comment.content = (
        comment.content if comment_update.content is None else comment_update.content
    )
    db.add(comment)
    db.commit()
    return comment


def delete_comment(db: Session, id: int, user_id: int):
    comment = find_comment_by_id(db, id, user_id)
    if comment is None:
        return None
    db.delete(comment)
    db.commit()
    return comment
