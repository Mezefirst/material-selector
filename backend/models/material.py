from sqlalchemy import Column, Integer, String, Float
from backend.database import Base

class Material(Base):
    __tablename__ = 'materials'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    type = Column(String, index=True)
    color = Column(String)
    strength = Column(Float)
    cost = Column(Float)
    sustainability = Column(Float)
    description = Column(String)
