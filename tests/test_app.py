from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_endpoint_exists():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "service": "Employee Management API"}

def test_create_employee_rejects_invalid_salary():
    response = client.post(
        "/employees/",
        json={"name": "Rahul", "department": "IT", "salary": -10},
    )
    # TODO: Assert the correct validation/error status.
    assert response.status_code == 422
