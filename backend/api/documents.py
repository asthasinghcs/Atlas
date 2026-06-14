from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.dependencies import get_db
from models.document import Document
from schemas.document import DocumentCreate
from schemas.document_response import DocumentResponse

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

    return {
        "message": "Document created successfully"
    }