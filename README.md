# 📚 Library Manager API

A RESTful Library Management API built with **FastAPI**, **SQLAlchemy**, **JWT Authentication**,**Alembic**, and **Pytest**.

## 🚀 Features

- User Registration
- User Login with JWT Authentication
- Password Hashing using bcrypt
- Protected Routes
- Create Book
- Get All Books
- Get Single Book
- Update Book
- Delete Book
- Dependency Injection with FastAPI
- Dependency Override for Testing
- Pytest Test Suite
- SQLite Test Database

---

## 🛠️ Tech Stack

- Python
- FastAPI
- SQLAlchemy
- Alembic
- SQLite / PostgreSQL
- JWT
- Passlib (bcrypt)
- Pytest
- Uvicorn

---

## 📁 Project Structure

```
library-manager-api/
│
├── routers/
│   ├── auth_routes.py
│   ├── books.py
│   └── users.py
│
├── tests/
│   ├── conftest.py
│   ├── test_auth.py
│   └── test_books.py
│
├── models.py
├── schemas.py
├── auth.py
├── database.py
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone <your_repo_url>

cd library-manager-api
```

Create virtual environment

```bash
python -m venv .venv
```

Activate environment

Windows

```bash
.venv\Scripts\activate
```

Linux/Mac

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

```
SECRET_KEY=your_secret_key

ALGORITHM=HS256

DATA_BASE_URL=your_database_url
```

---

## ▶️ Run Server

```bash
uvicorn main:app --reload
```

Visit:

```
http://127.0.0.1:8000/docs
```

for Swagger UI.

---

## 🧪 Running Tests

Run all tests

```bash
pytest
```

The project uses:

- Pytest Fixtures
- conftest.py
- Dependency Overrides
- Test Database

for isolated backend testing.

---

## 🔒 Authentication

Protected routes require a JWT token.

Login endpoint:

```
POST /auth/login
```

Use the returned Bearer Token for authenticated requests.

---

## 📌 Learning Objectives

This project was built to practice:

- REST API Development
- FastAPI Dependency Injection
- JWT Authentication
- SQLAlchemy ORM
- Database Relationships
- CRUD Operations
- Pytest
- Fixtures
- Dependency Overrides
- Test Databases

---

## 👨‍💻 Author

Built by **Tajik**