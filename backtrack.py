import json
import numpy as np
from board import Board
from validate import validate


def load(file_path: str) -> dict:
    try:
        with open(str(file_path), "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("ERROR - File Not Found")


def run(file_path: str = None):
    if not file_path:
        file_path = "puzzle.json"

    board_dict = load(file_path)

    solution = np.array(board_dict["solution"])
    puzzle = np.array(board_dict["puzzle"])

    s = Board(solution)
    p = Board(puzzle)


if __name__ == "__main__":
    run()
