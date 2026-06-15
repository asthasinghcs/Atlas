from sqlalchemy.orm import Session

from ingestion.rss_ingestor import fetch_rss_feed
from extraction.entity_extractor import extract_entities

from models.document import Document
from models.entity import Entity
from models.document_entity import DocumentEntity


def ingest_feed(
    feed_url: str,
    db: Session
):

    articles = fetch_rss_feed(feed_url)

    for article in articles:

        existing_document = (
            db.query(Document)
            .filter(Document.url == article["url"])
            .first()
        )

        if existing_document:
            continue

        document = Document(
            title=article["title"],
            content=article["content"],
            source="RSS",
            source_type="news",
            url=article["url"]
        )

        db.add(document)
        db.commit()
        db.refresh(document)

        entities = extract_entities(
            article["content"]
        )

        for item in entities:

            existing_entity = (
                db.query(Entity)
                .filter(
                    Entity.name == item["name"]
                )
                .first()
            )

            if existing_entity is None:

                existing_entity = Entity(
                    name=item["name"],
                    entity_type=item["entity_type"]
                )

                db.add(existing_entity)
                db.commit()
                db.refresh(existing_entity)

            link = DocumentEntity(
                document_id=document.id,
                entity_id=existing_entity.id
            )

            db.add(link)

        db.commit()