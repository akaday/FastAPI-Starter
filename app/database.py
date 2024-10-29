# app/database.py
from sqlalchemy import create_engine, MetaData

DATABASE_URL = "sqlite:///./test.db"
database = databases.Database(DATABASE_URL)
metadata = MetaData()

engine = create_engine(DATABASE_URL)
