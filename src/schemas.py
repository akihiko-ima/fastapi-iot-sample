from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


# ------------------------------------------------------
# User
# ------------------------------------------------------
class UserCreate(BaseModel):
    username: str = Field(min_length=2, examples=["testuser_1"])
    password: str = Field(min_length=8, examples=["test1234"])


class UserResponse(BaseModel):
    id: int = Field(gt=0, examples=[1])
    username: str = Field(min_length=2, examples=["testuser_1"])
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str


class DecodedToken(BaseModel):
    username: str
    user_id: int


# ------------------------------------------------------
# Comment
# ------------------------------------------------------
class CommentCreate(BaseModel):
    content: str = Field(min_length=4, examples=["sample_hogehoge_booboo"])


class CommentUpdate(BaseModel):
    content: str = Field(min_length=4, examples=["sample_hogehoge_booboo"])


class CommentResponse(BaseModel):
    id: int = Field(gt=0, examples=[1])
    content: str = Field(min_length=4, examples=["sample_hogehoge_booboo"])
    created_at: datetime
    updated_at: datetime
    user_id: int

    model_config = ConfigDict(from_attributes=True)
