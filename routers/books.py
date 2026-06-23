from models import Books
from schemas import Book,Book_Response,BookUpdate
from fastapi import Depends,HTTPException,APIRouter
from database import get_db
from auth import get_current_user
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
router = APIRouter(prefix="/books",tags=["/BOOKS"])
@router.post("/",status_code=201)
async def create_book(book:Book,db:AsyncSession=Depends(get_db),current_user=Depends(get_current_user)):
    book_data = Books(
        title = book.title,
        author = book.author,
        genre = book.genre,
        available = book.available,
        owner_id = current_user.id
    )
    db.add(book_data)
    await db.commit()
    await db.refresh(book_data)
    return book_data
@router.get("/",response_model=list[Book_Response])
async def all_books(db:AsyncSession=Depends(get_db),current_user=Depends(get_current_user)):
    result = await db.execute(select(Books).where(Books.owner_id == current_user.id))
    books = result.scalars().all()
    return books
@router.get("/{book_id}",response_model=Book_Response)
async def get_book(book_id:int,db:AsyncSession=Depends(get_db),current_user=Depends(get_current_user)):
    result = await db.execute(select(Books).where(Books.id == book_id,Books.owner_id == current_user.id))
    book = result.scalar_one_or_none()
    if not book:
        raise HTTPException(status_code=404,detail="book not found")
    return book
@router.put("/{book_id}",response_model=Book_Response)
async def update_book(book_id:int,update:BookUpdate,db:AsyncSession=Depends(get_db),current_user=Depends(get_current_user)):
    result = await db.execute(select(Books).where(Books.id == book_id,Books.owner_id == current_user.id))
    book = result.scalar_one_or_none()
    if not book:
        raise HTTPException(status_code=404,detail="book not found")
    if update.title is not None:
        book.title = update.title
    if update.genre is not None:
        book.genre = update.genre
    await db.commit()
    await db.refresh(book)
    return book
@router.delete("/{book_id}")
async def delete_book(book_id:int,db:AsyncSession=Depends(get_db),current_user = Depends(get_current_user)):
    result = await db.execute(select(Books).where(Books.id == book_id,Books.owner_id == current_user.id))
    book = result.scalar_one_or_none()
    if not book:
        raise HTTPException(status_code=404,detail="book not found")
    await db.delete(book)
    await db.commit()
    return {"success":"book deleted"}

    