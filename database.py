from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# -------------------------------
# DATABASE URL FROM ENVIRONMENT
# -------------------------------
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

# -------------------------------
# CREATE ENGINE
# -------------------------------
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Test connection
try:
    with engine.connect() as conn:
        print("✅ Database connected successfully!")
except Exception as e:
    print(f"❌ Database connection failed: {e}")

# -------------------------------
# SESSION LOCAL
# -------------------------------
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# -------------------------------
# BASE CLASS
# -------------------------------
Base = declarative_base()

# -------------------------------
# DEPENDENCY
# -------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()