from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Date
from sqlalchemy import DateTime

from db.base import Base


class TrendSnapshot(Base):
    __tablename__ = "trend_snapshots"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    snapshot_date = Column(
        Date,
        nullable=False,
        index=True
    )

    entity_name = Column(
        String,
        nullable=False,
        index=True
    )

    entity_type = Column(
        String,
        nullable=False
    )

    mentions = Column(
        Integer,
        nullable=False
    )

    influence_score = Column(
        Float,
        nullable=False
    )

    relationship_count = Column(
        Integer,
        nullable=False
    )

    theme = Column(
        String,
        nullable=True
    )
    
    article_count = Column(
    Integer,
    nullable=False,
    default=0
    )

    source_count = Column(
        Integer,
        nullable=False,
        default=0
    )

    first_seen = Column(
        DateTime,
        nullable=True
    )

    last_seen = Column(
        DateTime,
        nullable=True
    )