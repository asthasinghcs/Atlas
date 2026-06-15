from pydantic import BaseModel


class IngestionStats(BaseModel):
    articles_seen: int
    documents_created: int
    documents_skipped: int