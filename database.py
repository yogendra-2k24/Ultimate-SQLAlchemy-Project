from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

# Connected To Database 
class Base(DeclarativeBase):
    pass

DATABASE_URL = "postgresql+psycopg2://postgres:Yogesh123@localhost:5432/library_db"

engine = create_engine(DATABASE_URL,
    echo=True
)

SessionLocal = sessionmaker(bind=engine)