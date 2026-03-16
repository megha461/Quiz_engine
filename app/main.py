from fastapi import FastAPI
from .database import engine
from .models import Base

from .routers import ingest_router, quiz_router, student_router

app = FastAPI(title="Peblo Quiz Engine")

Base.metadata.create_all(bind=engine)

app.include_router(ingest_router.router)
app.include_router(quiz_router.router)
app.include_router(student_router.router)

@app.get("/")
def root():
    return {"message": "Peblo Quiz Engine Running"}