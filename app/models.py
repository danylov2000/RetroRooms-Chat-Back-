import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text, Table, ForeignKey
from sqlalchemy.orm import  relationship, declarative_base

Base = declarative_base()






room_user = Table(
    'room_users',
    Base.metadata,
    Column( 'room_id', ForeignKey("rooms.id"), primary_key=True),
    Column( 'user_id', ForeignKey("users.id"), primary_key=True)
)

class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True, autoincrement=True)
    author = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now())
    members = relationship("User", secondary=room_user, back_populates="rooms")



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    firebase_id = Column(String, unique=True, nullable=False, )
    rooms = relationship("Room", secondary=room_user, back_populates="members")
