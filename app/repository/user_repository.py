from typing import Any, Optional

from sqlalchemy.orm import Session

from app.model.AppUser import AppUser
from app.oauth.security import verify_password

class UserRepository():

  def get_by_id(self, db: Session, id: Any) -> Optional[AppUser]:
    return db.query(AppUser).filter(AppUser.user_id == id).first()

  def get_by_username(self, db: Session, *, username: str) -> Optional[AppUser]:
    return db.query(AppUser).filter(AppUser.username == username).first()

  def authenticate(self, db: Session, *, username: str, password: str) -> Optional[AppUser]:
    user = self.get_by_username(db, username=username)
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user

  def is_active(self, user: AppUser) -> bool:
    return user.is_active

userRepository = UserRepository()