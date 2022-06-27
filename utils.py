import json
from typing import Any


def load_json(file_path: str) -> Any:
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"ERROR - {file_path} Not Found!")


def save_json(file_path: str, obj: Any) -> None:
    try:
        with open(file_path, "w") as file:
            json.dump(obj, file)
    except:
        print("Error saving obj to json file in utils.py")
