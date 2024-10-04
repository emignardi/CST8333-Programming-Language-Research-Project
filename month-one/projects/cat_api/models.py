from sqlalchemy import Column, Integer, String
from db import Base

class Cat(Base):
    __tablename__ = "cats"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(25), nullable=False)
    colour = Column(String(25), nullable=False)