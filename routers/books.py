from models import Books
from schemas import Book,Book_Response,BookUpdate
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,APIRouter
from database import get_db
from auth import get_current_user
router = APIRouter(prefix="/books",tags=["/BOOKS"])
@router.post("/",status_code=201)
def create_book(book:Book,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    book_data = Books(
        title = book.title,
        author = book.author,
        genre = book.genre,
        available = book.available,
        owner_id = current_user.id
    )
    db.add(book_data)
    db.commit()
    db.refresh(book_data)
    return book_data
@router.get("/",response_model=list[Book_Response])
def get_books(genre:str|None=None,available:bool|None=None,limit:int=5,skip:int=10,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    books = db.query(Books).filter(Books.owner_id == current_user.id)
    if genre:
        books = db.query(Books).filter(Books.genre == genre)
    if available is not None:
        books = db.filter(Books.available == available)
    return books.offset(skip).limit(limit).all()
@router.get("/{book_id}",response_model=Book_Response)
def get_book(book_id:int,db:Session=Depends(get_db),current_user = Depends(get_current_user)):
    book = db.query(Books).filter(Books.id == book_id,Books.owner_id == current_user.id).first()
    if not book:
        raise HTTPException(status_code=404,detail="book not found")
    return book
@router.put("/{book_id}",response_model=Book_Response)
def update_book(book_id:int,update:BookUpdate,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    book = db.query(Books).filter(Books.id == book_id,Books.owner_id == current_user.id).first()
    if not book:
        raise HTTPException(status_code=404,detail="book not found")
    if update.title is not None:
        book.title = update.title
    if update.genre is not None:
        book.genre = update.genre
    db.commit()
    db.refresh(book)
    return book
@router.delete("/{book_id}")
def delete_book(book_id:int,db:Session=Depends(get_db),current_user = Depends(get_current_user)):
    book = db.query(Books).filter(Books.id == book_id,Books.owner_id == current_user.id).first()
    if not book:
        raise HTTPException(status_code=404,detail="book not found")
    db.delete(book)
    db.commit()
    return {"success":"book deleted"}

    