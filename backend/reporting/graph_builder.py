from collections import defaultdict

from sqlalchemy.orm import Session

from models.entity import Entity
from schemas.knowledge_graph import (
    GraphNode,
    GraphEdge,
    KnowledgeGraph,
)


def build_knowledge_graph(
    db: Session
) -> KnowledgeGraph:

    nodes = []
    edges = []

    entities = db.query(Entity).all()

    node_ids = set()
    from collections import defaultdict

    edge_weights = defaultdict(int)

    for entity in entities:

        if entity.name not in node_ids:

            nodes.append(
                GraphNode(
                    id=entity.name,
                    label=entity.name,
                    type=entity.entity_type.lower(),
                    frequency=len(entity.document_links)
                )
            )

            node_ids.add(entity.name)

        for link in entity.document_links:

            document = link.document

            for other_link in document.entity_links:

                other = other_link.entity

                if other.id == entity.id:
                    continue

                key = tuple(
                    sorted(
                        [
                            entity.name,
                            other.name
                        ]
                    )
                )

                edge_weights[key] += 1
                
                for (source, target), weight in edge_weights.items():

                    edges.append(
                        GraphEdge(
                            source=source,
                            target=target,
                            relation="co_occurs_with",
                            weight=weight
                        )
                    )

    return KnowledgeGraph(
        nodes=nodes,
        edges=edges 
    )