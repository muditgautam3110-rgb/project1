from pydantic import BaseModel, Field


class EmployeeCreate(BaseModel):
    name: str = Field(..., max_length=100)
    department: str = Field(..., max_length=100)
    salary: float = Field(..., ge=0)


class EmployeeRead(EmployeeCreate):
    id: int
