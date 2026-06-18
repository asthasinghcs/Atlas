from collections import Counter

from models.document_entity import DocumentEntity
from models.entity import Entity


def discover_relationships(
    entity_name: str,
    db,
    limit: int | None = None
):

    target = (
        db.query(Entity)
        .filter(
            Entity.name == entity_name
        )
        .first()
    )

    if target is None:
        return []

    document_links = (
        db.query(DocumentEntity)
        .filter(
            DocumentEntity.entity_id == target.id
        )
        .all()
    )

    counter = Counter()

    for document_link in document_links:

        related_links = (
            db.query(DocumentEntity)
            .filter(
                DocumentEntity.document_id
                == document_link.document_id
            )
            .all()
        )

        for related_link in related_links:

            if related_link.entity_id == target.id:
                continue

            counter[
                related_link.entity_id
            ] += 1

    if limit is None:
        related_entities = counter.most_common()
    else:
        related_entities = counter.most_common(limit)

    results = []

    for entity_id, count in related_entities:

        entity = (
            db.query(Entity)
            .filter(
                Entity.id == entity_id
            )
            .first()
        )

        if entity:

            results.append(
                {
                    "name": entity.name,
                    "co_occurrences": count
                }
            )

    return results