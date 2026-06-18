from collections import defaultdict

from sqlalchemy.orm import Session

from models.entity import Entity


def build_graph(db: Session):

    graph = defaultdict(set)

    entities = db.query(Entity).all()

    for entity in entities:

        for link in entity.document_links:

            document = link.document

            for other_link in document.entity_links:

                other = other_link.entity

                if other.id != entity.id:
                    graph[entity.name].add(other.name)

    return {
        node: sorted(list(neighbors))
        for node, neighbors in graph.items()
    }