from db.session import SessionLocal

from models.document import Document
from models.entity import Entity
from models.document_entity import DocumentEntity

from extraction.entity_extractor import (
    extract_entities
)


db = SessionLocal()

try:

    db.query(
        DocumentEntity
    ).delete()

    db.query(
        Entity
    ).delete()

    db.commit()

    documents = (
        db.query(Document)
        .all()
    )

    for document in documents:

        entities = extract_entities(
            document.content
        )

        for item in entities:

            entity = (
                db.query(Entity)
                .filter(
                    Entity.name == item["name"]
                )
                .first()
            )

            if entity is None:

                entity = Entity(
                    name=item["name"],
                    entity_type=item["entity_type"]
                )

                db.add(entity)
                db.commit()
                db.refresh(entity)

            link = DocumentEntity(
                document_id=document.id,
                entity_id=entity.id
            )

            db.add(link)

        db.commit()

    print(
        "Entity reprocessing completed."
    )

finally:

    db.close()