import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from database import Base,get_db
data_base_url = "sqlite:///./test.db"
engine = create_engine(data_base_url)
TestingSessionLocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)
Base.metadata.create_all(bind=engine)
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
@pytest.fixture
def client():
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()
      