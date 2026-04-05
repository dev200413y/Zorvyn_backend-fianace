from sqlalchemy.orm import Session
from app.models.record import FinancialRecord
from app.schemas.record import RecordBase,RecordUpdate
from fastapi import HTTPException
def create_record(db: Session, data: RecordBase, user_id: int):
    new_record = FinancialRecord(
        user_id=user_id,
        type=data.type,
        amount=data.amount,
        category=data.category,
        date=data.date,
        notes=data.notes
    )
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record

def get_records(db: Session, user_id:int, type: str = None, category: str = None):
    query = db.query(FinancialRecord).filter(FinancialRecord.user_id == user_id)
    if type:
        query = query.filter(FinancialRecord.type == type)
    if category:
        query = query.filter(FinancialRecord.category == category)
    return query.all()
    
def get_record_by_id(db: Session, record_id: int, user_id: int):
    record = db.query(FinancialRecord).filter(
        FinancialRecord.id == record_id, 
        FinancialRecord.user_id == user_id
        ).first()
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    return record   
def update_record(db: Session, record_id: int, data: RecordUpdate, user_id: int):
    record = get_record_by_id(db, record_id, user_id)
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(record, field, value)
    db.commit()
    db.refresh(record)
    return record

def delete_record(db: Session, record_id: int, user_id: int):
    record = get_record_by_id(db, record_id, user_id)
    db.delete(record)
    db.commit()
    return {"message": "Record deleted successfully"}