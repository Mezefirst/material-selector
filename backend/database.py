import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Support both PostgreSQL and SQLite with fallback
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    # Default fallback to SQLite for development
    DATABASE_URL = "sqlite:///./material_selector.db"
    
# Handle SQLAlchemy 2.0 compatibility
try:
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})
    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    Base = declarative_base()
except Exception as e:
    print(f"Database engine creation failed: {e}")
    # Create a dummy engine for graceful degradation
    engine = None
    SessionLocal = None
    Base = None
