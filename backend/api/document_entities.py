from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.dependencies import get_db
from models.document import Document


router = APIRouter(
    prefix="/document-entities",
    tags=["Document Entities"]
)


@router.get("/{document_id}")
def get_document_entities(
    document_id: int,
    db: Session = Depends(get_db)
):

    document = (
        db.query(Document)
        .filter(
            Document.id == document_id
        )
        .first()
    )

    if document is None:
        return {
            "error": "Document not found"
        }

    return {
        "document": document.title,
        "entities": [
            {
                "id": link.entity.id,
                "name": link.entity.name,
                "type": link.entity.entity_type
            }
            for link in document.entity_links
        ]
    }