from sqlalchemy import Column, Integer, String, Date
from .database import Base

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    application_date = Column(Date)
    status = Column(String, default="Applied")
    notes = Column(String)
    follow_up_date = Column(Date)