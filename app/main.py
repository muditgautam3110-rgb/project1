from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Employee Management API")
app.include_router(router)


@app.get("/health")
def health():
    return {"status": "healthy", "service": "Employee Management API"}
