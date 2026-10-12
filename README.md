# Employee Management API — Practical Evaluation

You are the developer assigned to finish this partially completed application.

## Business requirements
1. Provide a health endpoint.
2. Create and list employees through a FastAPI API.
3. Persist employees in PostgreSQL.
4. Validate employee names, departments, and positive salaries.
5. Import employees from CSV with validation and safe re-runs (idempotency).
6. Add automated tests.
7. Package the app with Docker and Docker Compose.
8. Add a CI workflow that runs tests and builds the image.

## Important
This project is intentionally incomplete. Do not replace everything with a new project.
Inspect what exists, identify gaps, and make small, testable changes.
Never commit passwords or `.env` files.

## Current intended stack
- Python 3.12
- FastAPI
- SQLAlchemy
- PostgreSQL
- pytest
- Docker Compose
- GitHub Actions

## Evaluation stages
- Stage 1: Inspect project, Git state, Python and Docker availability.
- Stage 2: Create/activate a virtual environment and install dependencies.
- Stage 3: Complete API validation and error handling.
- Stage 4: Configure PostgreSQL and implement persistence.
- Stage 5: Implement CSV import, schema validation, and idempotency.
- Stage 6: Write/run pytest tests.
- Stage 7: Diagnose Linux/CLI-style issues using PowerShell and container logs.
- Stage 8: Complete Dockerfile and Compose setup.
- Stage 9: Complete CI workflow and review Git changes.

Do not jump ahead; your mentor will assign one task at a time.
