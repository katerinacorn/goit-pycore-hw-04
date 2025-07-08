import os
from typing import List, Dict

ENCODING = "utf-8"
FILE_NAME = "data/cats.txt"


def get_cats_info(path: str) -> List[Dict[str, str]]:
    """
    Reads a file containing cat data and returns a list of dictionaries.
    Each dictionary contains the cat's id, name, and age.

    :param path: Relative path to the text file with cat data.
    :return: A list of dictionaries with keys 'id', 'name', and 'age'.
    """
    cats = []
    try:
        base_dir = os.path.dirname(__file__)
        full_path = os.path.join(base_dir, path)

        with open(full_path, "r", encoding=ENCODING) as file:
            for line in file:
                id, name, age = line.strip().split(",")
                cats.append({"id": id, "name": name, "age": age})
    except FileNotFoundError:
        print(f"File not found: {full_path}.")
    except Exception as e:
        print(f"Error occurred: {e}")
    return cats


print("Running tests...")

# Run test on valid file
result = get_cats_info(FILE_NAME)
print(result)
expected = [
    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
    {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
    {"id": "60b90c1c13067a15887e1ae3", "name": "Athena", "age": "6"},
    {"id": "60b90c2413067a15887e1ae4", "name": "Thanos", "age": "9"},
]

assert result == expected, f"Expected {expected}, but got {result}"

# Test non-existent file
result_missing = get_cats_info("nonexistent_file.txt")
assert result_missing == [], "Expected empty list for missing file"


print("All tests passed.")
