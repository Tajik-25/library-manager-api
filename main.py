from fastapi import FastAPI
app = FastAPI()
from routers.auth_routes import router as auth_router
from routers.books import router as book_router
from routers.users import router as user_router
app.include_router(auth_router)
app.include_router(book_router)
app.include_router(user_router)
@app.get("/")
def root():
    return {"message": "library manager api is running"}
import os
if __name__ == "main":
    import uvicorn
    port = int(os.environ.get("PORT",8000))
    uvicorn.run("main:app",host="0.0.0.0",port=port)
