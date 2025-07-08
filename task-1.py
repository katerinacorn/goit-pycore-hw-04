import os
from typing import Tuple

ENCODING = "utf-8"
FILE_NAME = "data/salaries.txt"


def parse_salary_line(line: str) -> int:
    """
    Parses a line containing a developer's name and salary, and returns the salary as an integer.

    :param line: A string in the format "Name,SALARY" (e.g., "Alex Korp,3000").
    :return: The salary as an integer. Returns 0 if the line is invalid or cannot be parsed.
    """
    try:
        _, salary = line.strip().split(",")
        return int(salary)
    except ValueError:
        print(f"Skipping invalid line: {line.strip()}")
        return None


def total_salary(path: str) -> Tuple[int, float]:
    """
    Calculates the total and average salary of developers listed in a file.

    :param path: The path to the salary data file.

    :return: A tuple with total salary and average salary.
    """
    total = 0
    count = 0

    try:
        base_dir = os.path.dirname(__file__)
        full_path = os.path.join(base_dir, path)

        with open(full_path, "r", encoding=ENCODING) as file:
            for line in file:
                salary = parse_salary_line(line)
                if salary is not None:
                    total += int(salary)
                    count += 1
    except FileNotFoundError:
        print(f"File not found: {path}")
        return (0, 0.0)
    except Exception as e:
        print(f"An error occurred: {e}")
        return (0, 0.0)

    average = total / count if count > 0 else 0.0
    return total, average


print("Running tests...")

# Run test on valid file
total, average = total_salary(FILE_NAME)
assert total == 6000, f"Expected total 6000, got {total}"
assert average == 2000, f"Expected average 2000, got {average}"

# Test for non-existent file
total, average = total_salary("non_existent.txt")
assert total == 0 and average == 0.0, "Expected (0, 0.0) for missing file"

# Test UnicodeDecodeError (create file with invalid UTF-8 bytes)
with open("invalid_encoding.txt", "wb") as f:
    f.write(b"\xff\xfe\xfd")  # invalid UTF-8 bytes
try:
    total, average = total_salary("invalid_encoding.txt")
    assert total == 0 and average == 0.0, "Expected (0, 0.0) for UnicodeDecodeError"
finally:
    os.remove("invalid_encoding.txt")


print("All tests passed.")
