from fastapi import APIRouter, UploadFile, File
from ..services.ingest_service import ingest_pdf

router = APIRouter()

@router.post("/ingest")
async def ingest(file: UploadFile = File(...)):
    content = await ingest_pdf(file)
    return {"message": "PDF processed", "chunks": content}