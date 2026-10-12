from sqlalchemy import Column, Integer, String, Float
from app.database import Base


class Employee(Base):
    # TODO: Define the table name and required columns/constraints.
    __tablename__ = "TODO"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    department = Column(String(100), nullable=False)
    salary = Column(Float, nullable=False)
