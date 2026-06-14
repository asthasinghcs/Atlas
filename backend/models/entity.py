from sqlalchemy import Column, Integer, String

from db.base import Base
from sqlalchemy.orm import relationship


class Entity(Base):
    __tablename__ = "entities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    entity_type = Column(String, nullable=False)
    document_links = relationship(
    "DocumentEntity",
    back_populates="entity"
)