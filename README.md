# 📚 Library Management API

A RESTful Library Management System built using **FastAPI**, **PostgreSQL**, and **SQLAlchemy ORM**. This project demonstrates backend development concepts including authentication, database operations, request validation, business logic, and REST API design.

---

##  Features

- User Registration & Login
- JWT Authentication
- Protected Routes
- Book Management (CRUD)
- Issue Book
- Return Book
- Filter Books
- Pagination
- Sorting
- Request Validation using Pydantic
- Response Models
- SQLAlchemy Relationships
- Password Hashing (Passlib + BCrypt)

---

## 🛠️ Tech Stack

- Python 3
- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Pydantic
- JWT Authentication
- OAuth2 Password Flow
- Passlib (BCrypt)
- Uvicorn

---

##  Project Structure (not industrially good bcoz it was my first project with fastapi & i only focused on tech-stack so i didnt care about the structure)

```text
Library-Management-API/
│
├── main.py
├── crud.py
├── auth.py
├── database.py
├── models.py
├── schemas.py
├── requirements.txt
└── README.md
```

---

##  API Endpoints

### Authentication

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/register` | Register a new user |
| POST | `/login` | Login and generate JWT Token |
| GET | `/me` | Get current logged-in user |

---

### Books

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/books` | Get all books |
| POST | `/books` | Add a new book |
| GET | `/books/{book_id}` | Get book by ID |
| PUT | `/books/{book_id}` | Update book |
| DELETE | `/books/{book_id}` | Delete book |
| GET | `/books/filter` | Filter books |

---

### Library Operations

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/return/{issue_id}` | Return issued book |

---

##  Authentication

This project uses **JWT (JSON Web Token)** for authentication.

Protected endpoints require a valid access token.

Example:

```text
Authorization: Bearer <your_access_token>
```

---

##  Concepts Implemented

- FastAPI Routing
- Dependency Injection
- SQLAlchemy ORM
- CRUD Operations
- Response Models
- Schema Inheritance
- Relationships
- Lazy Loading
- JWT Authentication
- OAuth2 Password Flow
- Password Hashing
- Request Validation
- Business Logic
- REST API Design

---

##  Run Locally

### Clone Repository

```bash
git clone https://github.com/<your-username>/Library-Management-API.git
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start Server

```bash
uvicorn main:app --reload
```

---

##  API Preview

<img width="1662" height="732" alt="Screenshot 2026-07-23 023053" src="https://github.com/user-attachments/assets/0995d1ba-bbce-41a9-8e24-a6906d37b0c8" />
<img width="1541" height="712" alt="Screenshot 2026-07-23 023013" src="https://github.com/user-attachments/assets/947f50b7-64f9-44b0-acee-30b698e2c070" />
<img width="1211" height="590" alt="Screenshot 2026-07-23 023115" src="https://github.com/user-attachments/assets/c49fccf4-438f-4344-9c94-f607bc7e5c27" />
<img width="1228" height="620" alt="Screenshot 2026-07-23 023132" src="https://github.com/user-attachments/assets/dba84b44-21fd-49a9-81ae-6fcf4f79fcf9" />



Example:

- Login Endpoint
- Books Endpoint
- JWT Authorization
- Return Book API

---

##  Learning Outcomes

This project was built to learn modern backend development using FastAPI. It covers API development, authentication, database design, ORM relationships, validation, and RESTful architecture.

---

## 👨‍💻 Author

**Yogendra Meshram**

Backend Developer | Python | FastAPI | PostgreSQL | AI Backend Engineering
