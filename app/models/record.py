from sqlalchemy import Column, Integer, String,Float, DateTime, ForeignKey,Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class FinancialRecord(Base):
    __tablename__ = "financial_records"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"),nullable=False)
    type = Column(String, nullable=False) 
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    date = Column(DateTime(timezone=True), nullable=False)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    owner = relationship("User", back_populates="records")