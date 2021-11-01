import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class RequestLog(Base):
  __tablename__ = 'request_log'
  request_id = Column(Integer, primary_key=True)
  request_body = Column(String(500))
  request_response = Column(String(500))
  request_timestamp = Column(String(50))


  def __init__(self, request_body, request_response, request_timestamp):
    self.request_body = request_body
    self.request_response = request_response
    self.request_timestamp = request_timestamp


  def __repr__(self):
    return '<RequestLog %r>' % self.request_id