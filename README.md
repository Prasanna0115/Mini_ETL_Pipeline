# Mini ETL Pipeline

## Project Overview
A simple Python ETL pipeline that extracts employee data from a CSV file, transforms the data, and loads the processed records into an output CSV file.

## Technologies Used

- Python
- CSV module
- Git and GitHub

## Project Structure

```
Mini_ETL_Pipeline/
├── employees.csv
├── etl.py
├── output/
│   └── processed_employees.csv
├── .gitignore
└── README.md
```

## ETL Workflow

1. **Extract:** Read employee records from `employees.csv`.
2. **Transform:** Clean employee names and calculate annual salaries.
3. **Load:** Save processed records to `output/processed_employees.csv`.

## How to Run

```
python etl.py
```

## Expected Result
The pipeline processes 120 employee records and generates a CSV containing employee details and annual salaries.
