
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
    invalid_count = 0

    for row in rows:
        employee_id = (row.get("employee_id") or "").strip()
        name = (row.get("name") or "").strip()
        department = (row.get("department") or "").strip()
        salary_text = (row.get("salary") or "").strip()

        if not employee_id or not name or not department:
            invalid_count += 1
            continue

        try:
            salary = float(salary_text)
        except ValueError:
            invalid_count += 1
            continue

        if salary < 0:
            invalid_count += 1
            continue

        processed.append({
            "employee_id": employee_id,
            "name": name.title(),
            "department": department,
            "salary": salary,
            "annual_salary": salary * 12
        })

    return processed, invalid_count


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
    cleaned_rows, invalid_count = transform(rows)
    load(cleaned_rows)

    print(f"Extracted records: {len(rows)}")
    print(f"Processed records: {len(cleaned_rows)}")
    print(f"Invalid records skipped: {invalid_count}")
    print(f"Output saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
