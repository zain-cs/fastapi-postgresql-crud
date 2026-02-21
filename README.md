# FastAPI + PostgreSQL CRUD API

A RESTful API built with FastAPI and PostgreSQL for managing posts.

## Features
- ✅ Create, Read, Update, Delete (CRUD) operations
- ✅ PostgreSQL database with SQLAlchemy ORM
- ✅ Pydantic schemas for data validation
- ✅ Auto-generated API documentation

## Setup

1. **Clone the repository**
```bash
   git clone <your-repo-url>
   cd <repo-name>
```

2. **Create virtual environment**
```bash
   python -m venv venv
```

3. **Activate virtual environment**
```bash
   # Windows PowerShell
   .\venv\Scripts\Activate.ps1
   
   # Windows CMD
   .\venv\Scripts\activate.bat
   
   # Mac/Linux
   source venv/bin/activate
```

4. **Install dependencies**
```bash
   pip install -r requirements.txt
```

5. **Create `.env` file**
```bash
   # Create .env file in the root directory
   DATABASE_URL=postgresql://username:password@localhost:5432/database_name
   SECRET_KEY=your-secret-key-here
```

6. **Run the application**
```bash
   uvicorn main:app --reload
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/posts` | Get all posts |
| POST | `/posts` | Create a new post |
| GET | `/posts/{id}` | Get post by ID |
| PUT | `/posts/{id}` | Update post by ID |
| DELETE | `/posts/{id}` | Delete post by ID |

## API Documentation
After running the app, visit:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## Technologies Used
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Uvicorn