from pydantic import BaseModel, Field


class EmployeeCreate(BaseModel):
    # TODO: Add validation to these fields.
    name: str
    department: str
    salary: float


class EmployeeRead(EmployeeCreate):
    id: int
