from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.utils.jwt import verify_token
from fastapi.security import OAuth2PasswordBearer
from app.schemas.user import UserResponse,UserUpdate
from app.models.user import User

router = APIRouter(prefix="/users", tags=["users"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    return payload

@router.get("/me", response_model=UserResponse)
def get_me(db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_user = db.query(User).filter(User.id == int(user["sub"])).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/", response_model=list[UserResponse])
def get_all_users(db: Session = Depends(get_db),user=Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="admin access required")
    return db.query(User).all()

@router.put("/me", response_model=UserResponse)
def update_me(data: UserUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_user = db.query(User).filter(User.id == int(user["sub"])).first()
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(db_user, field, value)
    db.commit()
    db.refresh(db_user)
    return db_user