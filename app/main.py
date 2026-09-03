from fastapi import FastAPI
from app import models
from app.database import engine

app = FastAPI(title="Task API", version="0.1.0")

models.Base.metadata.create_all(bind=engine)

@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}