import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# TODO: Read DATABASE_URL safely and configure the engine/session.
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg://employee_user:change_me@localhost:5432/employee_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
