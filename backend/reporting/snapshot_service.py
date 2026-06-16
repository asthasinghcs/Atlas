from models.entity import Entity
from models.document_entity import (
    DocumentEntity
)
from models.entity_metric import (
    EntityMetric
)

from reporting.influence import (
    calculate_influence
)


def capture_snapshot(db):

    entities = (
        db.query(Entity)
        .all()
    )

    for entity in entities:

        mentions = (
            db.query(DocumentEntity)
            .filter(
                DocumentEntity.entity_id
                == entity.id
            )
            .count()
        )

        influence = (
            calculate_influence(
                entity.name,
                mentions,
                db
            )
        )

        metric = EntityMetric(
            entity_name=entity.name,
            mentions=mentions,
            relationship_strength=
                influence[
                    "relationship_strength"
                ],
            influence_score=
                influence[
                    "influence_score"
                ]
        )

        db.add(metric)

    db.commit()