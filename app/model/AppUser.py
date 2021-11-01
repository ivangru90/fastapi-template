import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime

Base = declarative_base()

class AppUser(Base):
  __tablename__ = 'app_user'
  user_id = Column(Integer, primary_key=True)
  username = Column(String(50))
  user_type = Column(String(50))
  email = Column(String(100))
  password = Column(String(200))
  is_active = Column(Boolean)
  registration_date = Column(DateTime)


  def __init__(self, username, user_type, email, password, is_active, registration_date):
    self.username = username
    self.user_type = user_type
    self.email = email
    self.password = password
    self.is_active = is_active
    self.registration_date = registration_date


  def __repr__(self):
    return '<AppUser %r>' % self.user_id