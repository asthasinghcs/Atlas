from pydantic import BaseModel
from datetime import datetime


class DocumentResponse(BaseModel):
    id: int
    title: str
    content: str
    source: str
    source_type: str
    url: str | None
    published_at: datetime | None
    ingested_at: datetime | None

    model_config = {
        "from_attributes": True
    }