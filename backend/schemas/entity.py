from pydantic import BaseModel


class EntityCreate(BaseModel):
    name: str
    entity_type: str