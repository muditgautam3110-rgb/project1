# import csv


# def import_employees_csv(path: str):
#     # TODO:
#     # - validate required headers
#     # - validate values and types
#     # - report malformed rows clearly
#     # - save records using the project's database layer
#     # - make repeated imports safe (idempotent)
#     with open(path, newline="", encoding="utf-8") as file:
#         return list(csv.DictReader(file))
import csv
from typing import List, Dict, Tuple

def import_employees_csv(path: str):
    required_headers = {"employee_id", "name", "email", "department"}

    errors = []
    valid_rows = []

    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        missing = required_headers - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"Missing required columns: {sorted(missing)}")

        for row_number, row in enumerate(reader, start=2):
            # validate row values
            if not row.get("employee_id"):
                errors.append(f"Row {row_number}: employee_id is required")
                continue

            if not row.get("email") or "@" not in row["email"]:
                errors.append(f"Row {row_number}: invalid email")
                continue

            # example: check for duplicates in current import
            if row["employee_id"] in {r["employee_id"] for r in valid_rows}:
                errors.append(f"Row {row_number}: duplicate employee_id")
                continue

            valid_rows.append({
                "employee_id": row["employee_id"],
                "name": row["name"].strip(),
                "email": row["email"].strip(),
                "department": row["department"].strip(),
            })

    if errors:
        return {
            "imported": [],
            "errors": errors,
        }

    return {
        "imported": valid_rows,
        "errors": [],
    }