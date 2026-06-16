from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

from datetime import datetime

from db.base import Base


class EntityMetric(Base):

    __tablename__ = "entity_metrics"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    entity_name = Column(
        String,
        nullable=False
    )

    mentions = Column(
        Integer,
        nullable=False
    )

    relationship_strength = Column(
        Integer,
        nullable=False
    )

    influence_score = Column(
        Integer,
        nullable=False
    )

    captured_at = Column(
        DateTime,
        default=datetime.utcnow
    )