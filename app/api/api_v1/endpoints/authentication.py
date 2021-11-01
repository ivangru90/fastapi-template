from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Body, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api import depends
from app.schema.token import Token 
from app.repository.user_repository import userRepository
from app.settings import settings
from app.oauth.security import create_access_token

router = APIRouter()

@router.post("/token", response_model=Token)
def login_access_token(
  db: Session = Depends(depends.get_db),
  form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
  """
  OAuth2 compatible token login, get an access token for future requests
  """
  user = userRepository.authenticate(db=db, username=form_data.username, password=form_data.password)
  if not user:
    raise HTTPException(status_code=400, detail="Incorrect username or password")
  elif not userRepository.is_active(user):
    raise HTTPException(status_code=400, detail="Inactive user")
  access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
  return {
    "access_token": create_access_token(
        user.user_id, expires_delta=access_token_expires
    ),
    "token_type": "bearer",
  }