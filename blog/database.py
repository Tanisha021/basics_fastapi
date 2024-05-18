from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHAMY_DATABASE_URL = 'sqlite:///./blog.db'
# now create the engine
engine = create_engine(SQLALCHAMY_DATABASE_URL,connect_args={"check_same_thread": False})

# Creating a Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declare a Mapping
Base = declarative_base()

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()