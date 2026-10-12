from pydantic import BaseModel, Field


class EmployeeCreate(BaseModel):
    # TODO: Add validation to these fields.
    name: str = Field(..., max_length=100)
    department: str = Field(..., max_length=100)
    salary: float = Field(..., ge=0)


class EmployeeRead(EmployeeCreate):
    id: int
