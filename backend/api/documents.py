from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.dependencies import get_db
from models.document import Document
from schemas.document import DocumentCreate
from schemas.document_response import DocumentResponse
from fastapi import APIRouter, Depends, HTTPException
from extraction.entity_extractor import extract_entities
from models.entity import Entity
from models.document_entity import DocumentEntity

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.get("/", response_model=list[DocumentResponse])
def get_documents(
    db: Session = Depends(get_db)
):
    documents = db.query(Document).all()

    return documents

@router.get("/{document_id}", response_model=DocumentResponse)
def get_document(
    document_id: int,
    db: Session = Depends(get_db)
):
    document = (
        db.query(Document)
        .filter(Document.id == document_id)
        .first()
    )

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    return document

@router.post("/")
def create_document(
    document: DocumentCreate,
    db: Session = Depends(get_db)
):
    db_document = Document(
        title=document.title,
        content=document.content,
        source=document.source,
        source_type=document.source_type,
        url=document.url
    )

    db.add(db_document)
    db.commit()
    db.refresh(db_document)

    entities = extract_entities(document.content)

    for item in entities:

        existing_entity = (
            db.query(Entity)
            .filter(Entity.name == item["name"])
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
            document_id=db_document.id,
            entity_id=existing_entity.id
        )

        db.add(link)

    db.commit()

    return {
        "message": "Document created successfully"
    }