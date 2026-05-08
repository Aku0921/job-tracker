from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import SessionLocal
from .. import crud, schemas

from typing import Optional


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get(
    "/dashboard/stats",
    response_model=schemas.DashboardStats
)
def dashboard_stats(db: Session = Depends(get_db)):
    return crud.get_dashboard_stats(db)


@router.post("/applications", response_model=schemas.ApplicationResponse)
def create_application(
    application: schemas.ApplicationCreate,
    db: Session = Depends(get_db)
):
    return crud.create_application(db, application)


@router.get("/applications")
def get_all_applications(
    status: Optional[str] = None,
    db: Session = Depends(get_db)
):
    return crud.get_applications(db, status)

@router.get("/applications/search")
def search_applications(
    keyword: str,
    db: Session = Depends(get_db)
):
    return crud.search_applications(db, keyword)

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

@router.put(
    "/applications/{application_id}",
    response_model=schemas.ApplicationResponse
)
def update_application(
    application_id: int,
    updated_data: schemas.ApplicationUpdate,
    db: Session = Depends(get_db)
):
    application = crud.update_application(
        db,
        application_id,
        updated_data
    )

    if not application:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    return application