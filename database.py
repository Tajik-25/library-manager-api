from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.orm import declarative_base,sessionmaker
from config import DATA_BASE_URL
engine = create_async_engine(DATA_BASE_URL)
AsyncSessionLocal = sessionmaker(class_=AsyncSession,autoflush=False,autocommit=False,bind=engine,expire_on_commit=False)
Base = declarative_base()
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session