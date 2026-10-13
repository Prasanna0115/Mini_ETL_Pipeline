
import csv
from pathlib import Path

INPUT_FILE = Path("employees.csv")
OUTPUT_DIR = Path("output")
OUTPUT_FILE = OUTPUT_DIR / "processed_employees.csv"


def extract():
    with INPUT_FILE.open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def transform(rows):
    processed = []

    for row in rows:
        name = row["name"].strip()
        department = row["department"].strip()
        salary = float(row["salary"])

        if not name or salary < 0:
            continue

        processed.append({
            "employee_id": row["employee_id"].strip(),
            "name": name.title(),
            "department": department,
            "salary": salary,
            "annual_salary": salary * 12
        })

    return processed


def load(rows):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    fields = [
        "employee_id",
        "name",
        "department",
        "salary",
        "annual_salary"
    ]

    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main():
    rows = extract()
    cleaned_rows = transform(rows)
    load(cleaned_rows)

    print(f"Extracted records: {len(rows)}")
    print(f"Processed records: {len(cleaned_rows)}")
    print(f"Output saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
