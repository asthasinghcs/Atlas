from sqlalchemy import Column, ForeignKey, Integer

from db.base import Base
from sqlalchemy.orm import relationship


class DocumentEntity(Base):
    __tablename__ = "document_entities"

    id = Column(Integer, primary_key=True, index=True)

    document_id = Column(
        Integer,
        ForeignKey("documents.id"),
        nullable=False
    )

    entity_id = Column(
        Integer,
        ForeignKey("entities.id"),
        nullable=False
    )

    document = relationship(
        "Document",
        back_populates="entity_links"
    )

    entity = relationship(
        "Entity",
        back_populates="document_links"
    )