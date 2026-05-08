from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import SessionLocal
from .. import crud, schemas


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/applications", response_model=schemas.ApplicationResponse)
def create_application(
    application: schemas.ApplicationCreate,
    db: Session = Depends(get_db)
):
    return crud.create_application(db, application)


@router.get("/applications")
def get_all_applications(db: Session = Depends(get_db)):
    return crud.get_applications(db)


@router.get("/applications/{application_id}")
def get_application(application_id: int, db: Session = Depends(get_db)):
    application = crud.get_application_by_id(db, application_id)

    if not application:
        raise HTTPException(status_code=404, detail="Application not found")

    return application


@router.delete("/applications/{application_id}")
def delete_application(application_id: int, db: Session = Depends(get_db)):
    application = crud.delete_application(db, application_id)

    if not application:
        raise HTTPException(status_code=404, detail="Application not found")

    return {"message": "Application deleted successfully"}