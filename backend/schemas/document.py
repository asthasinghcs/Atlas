from pydantic import BaseModel


class DocumentCreate(BaseModel):
    title: str
    content: str
    source: str
    source_type: str
    url: str | None = None