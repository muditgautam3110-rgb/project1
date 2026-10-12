import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# TODO: Read DATABASE_URL safely and configure the engine/session.
DATABASE_URL = os.getenv("DATABASE_URL", "REPLACE_ME")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
