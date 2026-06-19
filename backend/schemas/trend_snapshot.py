from datetime import date
from datetime import datetime

from pydantic import BaseModel


class TrendSnapshotResponse(BaseModel):

    snapshot_date: date

    entity_name: str

    entity_type: str

    mentions: int

    influence_score: float

    relationship_count: int

    article_count: int

    source_count: int

    first_seen: datetime | None = None

    last_seen: datetime | None = None

    theme: str | None = None


class TrendSnapshotCreate(
    TrendSnapshotResponse
):
    pass