from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = 'postgresql://postgres:postgres@localhost:5433/python_db'

DATABASE_URL = 'postgresql://postgres:saDASai128!@db.rlhstznswtigrzrdrpdv.supabase.co:5432/postgres'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
