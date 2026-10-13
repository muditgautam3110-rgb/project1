from fastapi import APIRouter
from app.schemas import EmployeeCreate
from app.database import SessionLocal
from app.models import Employee

router = APIRouter(prefix="/employees", tags=["employees"])


@router.post("/")
def create_employee(employee: EmployeeCreate):
    with SessionLocal() as db:
        db_employee = Employee(**employee.dict())
        db.add(db_employee)
        db.commit()
        db.refresh(db_employee)
        return db_employee


@router.get("/")
def list_employees():
    with SessionLocal() as db:
        return db.query(Employee).all()
