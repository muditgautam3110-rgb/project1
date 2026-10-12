from fastapi import APIRouter, HTTPException
from app.schemas import EmployeeCreate

router = APIRouter(prefix="/employees", tags=["employees"])


@router.post("/")
def create_employee(employee: EmployeeCreate):
    # TODO: Persist the employee to PostgreSQL and return the created record.
    raise HTTPException(status_code=501, detail="Not implemented")


@router.get("/")
def list_employees():
    # TODO: Read employee records from PostgreSQL.
    raise HTTPException(status_code=501, detail="Not implemented")
