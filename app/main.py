from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Employee Management API")
app.include_router(router)


@app.get("/health")
def health():
    # TODO: Return a useful health response.
    return {"status": "healthy"}
