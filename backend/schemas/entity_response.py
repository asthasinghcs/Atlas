from pydantic import BaseModel


class EntityResponse(BaseModel):
    id: int
    name: str
    entity_type: str

    model_config = {
        "from_attributes": True
    }