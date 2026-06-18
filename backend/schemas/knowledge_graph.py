from pydantic import BaseModel
from typing import Literal


class GraphNode(BaseModel):
    id: str
    label: str
    type: Literal[
        "person",
        "organization",
        "location",
        "product",
        "event",
        "theme",
        "document",
    ]
    frequency: int


class GraphEdge(BaseModel):
    source: str
    target: str
    relation: str
    weight: float


class KnowledgeGraph(BaseModel):
    nodes: list[GraphNode]
    edges: list[GraphEdge]