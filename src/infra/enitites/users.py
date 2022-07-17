from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from src.infra.config import Base


class Users(Base):
    """
    Users Entity.
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    pet_id = relationship("Pets")

    def __repr__(self):
        return f"User [name={self.name}]"
