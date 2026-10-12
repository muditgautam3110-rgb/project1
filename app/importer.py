import csv


def import_employees_csv(path: str):
    # TODO:
    # - validate required headers
    # - validate values and types
    # - report malformed rows clearly
    # - save records using the project's database layer
    # - make repeated imports safe (idempotent)
    with open(path, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))
