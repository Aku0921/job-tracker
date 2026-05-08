from sqlalchemy.orm import Session
from . import models, schemas


def create_application(db: Session, application: schemas.ApplicationCreate):
    db_application = models.Application(
        company_name=application.company_name,
        role=application.role,
        application_date=application.application_date,
        status=application.status,
        notes=application.notes,
        follow_up_date=application.follow_up_date
    )

    db.add(db_application)
    db.commit()
    db.refresh(db_application)

    return db_application


def get_applications(db: Session):
    return db.query(models.Application).all()


def get_application_by_id(db: Session, application_id: int):
    return db.query(models.Application).filter(
        models.Application.id == application_id
    ).first()


def delete_application(db: Session, application_id: int):
    application = db.query(models.Application).filter(
        models.Application.id == application_id
    ).first()

    if application:
        db.delete(application)
        db.commit()

    return application

def update_application(
    db: Session,
    application_id: int,
    updated_data: schemas.ApplicationUpdate
):
    application = db.query(models.Application).filter(
        models.Application.id == application_id
    ).first()

    if not application:
        return None

    application.company_name = updated_data.company_name
    application.role = updated_data.role
    application.application_date = updated_data.application_date
    application.status = updated_data.status
    application.notes = updated_data.notes
    application.follow_up_date = updated_data.follow_up_date

    db.commit()
    db.refresh(application)

    return application