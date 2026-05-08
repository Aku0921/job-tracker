from pydantic import BaseModel
from datetime import date
from typing import Optional


class ApplicationCreate(BaseModel):
    company_name: str
    role: str
    application_date: date
    status: Optional[str] = "Applied"
    notes: Optional[str] = None
    follow_up_date: Optional[date] = None


class ApplicationResponse(ApplicationCreate):
    id: int

    class Config:
        from_attributes = True

class ApplicationUpdate(BaseModel):
    company_name: str
    role: str
    application_date: date
    status: Optional[str] = None
    notes: Optional[str] = None
    follow_up_date: Optional[date] = None

class DashboardStats(BaseModel):
    total: int
    applied: int
    interview: int
    rejected: int
    selected: int