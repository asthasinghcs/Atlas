from sqlalchemy import Column, DateTime, Integer, String, Text

from db.base import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    content = Column(Text, nullable=False)

    source = Column(String, nullable=False)

    source_type = Column(String, nullable=False)

    url = Column(String)

    published_at = Column(DateTime)

    ingested_at = Column(DateTime)