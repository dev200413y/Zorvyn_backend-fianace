from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.record import RecordBase,RecordUpdate,RecordResponse
from app.services.record_service import (
    create_record, get_records,get_record_by_id, update_record, delete_record)
from app.utils.jwt import verify_token
from fastapi import APIRouter,Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
router = APIRouter(prefix="/records", tags=["records"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")    
    return payload

@router.post("/", response_model=RecordResponse)
def create(data: RecordBase, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return create_record(db, data, int(user["sub"]))

@router.get("/")
def get_all(type: str = None, category: str = None, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return get_records(db, int(user["sub"]), type, category)

@router.get("/{record_id}")
def get_one(record_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return get_record_by_id(db, record_id, int(user["sub"]))

@router.put("/{record_id}")
def update(record_id: int, data: RecordUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return update_record(db, record_id, data, int(user["sub"]))

@router.delete("/{record_id}")
def delete(record_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return delete_record(db, record_id, int(user["sub"]))