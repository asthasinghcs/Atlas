from collections import defaultdict

from sqlalchemy.orm import Session

from models.entity import Entity


def compute_influence_scores(
    db: Session
):

    scores = defaultdict(int)

    entities = db.query(Entity).all()

    for entity in entities:

        scores[entity.name] += len(
            entity.document_links
        )

        for link in entity.document_links:

            document = link.document

            scores[entity.name] += len(
                document.entity_links
            )

    ranked = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return [
        {
            "entity": entity,
            "score": score
        }
        for entity, score in ranked
    ]