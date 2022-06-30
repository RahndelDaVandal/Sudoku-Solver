import json
from pathlib import Path
from datetime import datetime
from datetime import datetime
from typing import Any
from dataclasses import dataclass


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
    except Exception as e:
        print(f"Error saving obj to json file in utils.py\n\n{e}")


@dataclass
class Logger:
    log_str: str = ""

    def __post_init__(self):
        dt = datetime.now()
        ts = dt.strftime("%m-%d-%yT%H-%M-%S")
        file_name = f"LOG--{ts}.log"
        self.file_path = str(Path(__file__).parent / file_name)

    def __call__(self, log_text: str) -> None:
        self.log_str += f"{log_text}\n"
        self.append_log(log_text)

    def log(self, log_text: str) -> None:
        self.log_str += f"{log_text}\n"

    def show(self) -> None:
        print(self.log_str)

    def get_log(self) -> str:
        return self.log_str

    def append_log(self, text: str) -> None:
        try:
            with open(self.file_path, "a") as file:
                file.write(text + "\n")
        except Exception as e:
            print(e)

    def log_to_file(self, file_dir: str, log: str, app_name: str = None) -> None:
        dt = datetime.now()
        ts = dt.strftime("%m-%d-%yT%H-%M-%S")
        if not app_name:
            app_name = ""
        else:
            app_name = "_" + app_name

        file_name = f"{ts}{app_name}.log"

        try:
            with open(str(file_dir + "/" + file_name), "w") as file:
                file.write(log)
        except Exception as e:
            print(e)
