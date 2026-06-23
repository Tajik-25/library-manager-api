from fastapi import APIRouter,Depends
from auth import get_current_user
from sqlalchemy.ext.asyncio import AsyncSession
router = APIRouter(prefix="/users",tags=["/USERS"])
@router.get("/me")
async def get_me(current_user = Depends(get_current_user)):
    return current_user
