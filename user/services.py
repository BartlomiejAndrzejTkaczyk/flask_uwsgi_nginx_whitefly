from __future__ import annotations

from common.database import SessionLocal

from common.security import hashing_password
from common.models import User


def find_user_by(nickname: str) -> User | None:
    db = SessionLocal()
    user = db.query(User).filter(User.nickname == nickname).first()

    return user


def create_user(nickname: str, password: str, info: str) -> User:
    db = SessionLocal()

    try:
        user = User(nickname=nickname, hash_password=hashing_password(password), info=info)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    finally:
        db.close()
