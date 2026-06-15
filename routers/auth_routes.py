from auth import create_access_token,verify_password,hash_password
from fastapi import Depends,HTTPException,APIRouter
from models import Users
from schemas import User
from fastapi.security import OAuth2PasswordRequestForm
from database import get_db
from sqlalchemy.orm import Session
router = APIRouter(prefix="/auth",tags=["/AUTHS"])
@router.post("/register",status_code=201)
def register_user(user:User,db:Session=Depends(get_db)):
    hashed_password = hash_password(user.password)
    user_data = Users(
        email = user.email,
        hashed_password = hashed_password
    )
    existing = db.query(Users).filter(Users.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400,detail="user already exists")
    db.add(user_data)
    db.commit()
    db.refresh(user_data)
    return user_data
@router.post("/login",status_code=200)
def login_user(form_data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user = db.query(Users).filter(Users.email == form_data.username).first()
    if not user:
        raise HTTPException(status_code=404,detail="user not found")
    valid = verify_password(form_data.password,user.hashed_password)
    if not valid:
        raise HTTPException(status_code=401,detail="unauthorized")
    token = create_access_token({"sub":user.email})
    return {"access_token":token,"token_type":"bearer"}
