from typing import Optional

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


def fake_decode_token(token):
    return User(
        username=token + 'fakedecoded', email='john@example.com', full_name='John Doe'
    )
