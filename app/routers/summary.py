from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.summary_service import get_summary, get_category_breakdown, get_monthly_summary
from app.utils.jwt import verify_token
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(prefix="/summary", tags=["summary"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    return payload

@router.get("/")
def summary(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return get_summary(db, int(user["sub"]))

@router.get("/categories")
def category_breakdown(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return get_category_breakdown(db, int(user["sub"])) 

@router.get("/monthly")
def monthly_summary(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return get_monthly_summary(db, int(user["sub"]))

