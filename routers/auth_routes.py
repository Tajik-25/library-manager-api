from auth import create_access_token,verify_password,hash_password
from fastapi import Depends,HTTPException,APIRouter
from models import Users
from schemas import User
from fastapi.security import OAuth2PasswordRequestForm
from database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
router = APIRouter(prefix="/auth",tags=["/AUTHS"])
@router.post("/register",status_code=201)
async def register_user(user:User,db:AsyncSession=Depends(get_db)):
    result = await db.execute(select(Users).where(Users.email == user.email))
    existing = result.scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=404,detail="user already exists")
    hashed_password = hash_password(user.password)
    user_data = Users(
        email = user.email,
        hashed_password = hashed_password
    )
    db.add(user_data)
    await db.commit()
    await db.refresh(user_data)
    return user_data
@router.post("/login",status_code=200)
async def login_user(form_data:OAuth2PasswordRequestForm=Depends(),db:AsyncSession=Depends(get_db)):
    result = await db.execute(select(Users).where(Users.email == form_data.username))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404,detail="user not found")
    valid = verify_password(form_data.password,user.hashed_password)
    if not valid:
        raise HTTPException(status_code=401,detail="unauthorized")
    token = create_access_token({"sub":user.email})
    return {"access_token":token,"token_type":"bearer"}
