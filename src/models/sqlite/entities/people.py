from dataclasses import dataclass
from sqlalchemy import Column, String, BIGINT, ForeignKey

from src.models.sqlite.settings.base import Base

class PeopleTable(Base):
    __tablename__ = "people"

    id          = Column(BIGINT, primary_key=True)
    first_name  = Column(String, nullable=False)
    last_name   = Column(String, nullable=False)
    age         = Column(BIGINT, nullable=False)
    pet_id      = Column(BIGINT, ForeignKey("pets.id"))

    
    def __repr__(self):
        return f"Pets [name={self.name}, last_name={self.type}, pet_id={self.pet_id}]"

@dataclass
class PersonWithoutId:
    age: int
    pet_id: int
    last_name: str
    first_name: str