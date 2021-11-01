from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app.db.session import Session
from app.model.AppUser import AppUser
from app.settings import settings
from app.schema.token import TokenPayload 
from app.repository.user_repository import userRepository


reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/token"
)


def get_db() -> Generator:
  try:
      db = Session()
      yield db
  finally:
      db.close()

def check_token(
    db: Session = Depends(get_db),
    token: str = Depends(reusable_oauth2)
) -> AppUser:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = userRepository.get_by_id(db, id=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user