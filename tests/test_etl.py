import unittest

from etl import transform


class TestETLTransform(unittest.TestCase):
    def test_valid_employee(self):
        rows = [{
            "employee_id": "101",
            "name": "prasanna reddy",
            "department": "Data Engineering",
            "salary": "30000",
        }]

        processed, invalid_count = transform(rows)

        self.assertEqual(len(processed), 1)
        self.assertEqual(processed[0]["name"], "Prasanna Reddy")
        self.assertEqual(processed[0]["annual_salary"], 360000)
        self.assertEqual(invalid_count, 0)

    def test_missing_name(self):
        rows = [{
            "employee_id": "102",
            "name": "",
            "department": "Analytics",
            "salary": "40000",
        }]

        processed, invalid_count = transform(rows)

        self.assertEqual(len(processed), 0)
        self.assertEqual(invalid_count, 1)

    def test_invalid_salary(self):
        for salary in ("not-a-number", "-1"):
            with self.subTest(salary=salary):
                rows = [{
                    "employee_id": "103",
                    "name": "Alex Smith",
                    "department": "Analytics",
                    "salary": salary,
                }]

                processed, invalid_count = transform(rows)

                self.assertEqual(len(processed), 0)
                self.assertEqual(invalid_count, 1)

    def test_negative_salary(self):
        rows = [{
            "employee_id": "104",
            "name": "Priya",
            "department": "HR",
            "salary": "-5000",
        }]

        processed, invalid_count = transform(rows)

        self.assertEqual(len(processed), 0)
        self.assertEqual(invalid_count, 1)


if __name__ == "__main__":
    unittest.main()
