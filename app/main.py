from fastapi import FastAPI
from .database import engine, Base
from .routes import jobs


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(jobs.router)


@app.get("/")
def home():
    return {"message": "Job Tracker API Running"}