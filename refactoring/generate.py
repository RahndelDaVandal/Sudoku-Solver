import json
import copy
from typing import List
from pathlib import Path
from random import sample


def pattern(r, c):
    """Returns Pattern for Baseline Valid Solution"""
    return (base * (r % base) + r // base + c) % side


def shuffle(s):
    """Suffle Function"""
    return sample(s, len(s))


base = 3
side = base * base


def gen_solution() -> List[list]:
    """Generates a Valid Sudoku Board"""
    rBase = range(base)
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, base * base + 1))
    return [[nums[pattern(r, c)] for c in cols] for r in rows]


def gen_puzzle(solution_board: List[list]) -> List[list]:
    """
    Takes a valid Sudoku Board and removes cell values
    to create a Sudoku puzzle
    """
    puzzle = copy.deepcopy(solution_board)
    squares = side * side
    empties = squares * 3 // 4
    for p in sample(range(squares), empties):
        puzzle[p // side][p % side] = 0
    return puzzle


def display(board: List[list]) -> None:
    """Prints Board to Screen"""
    numSize = len(str(side))
    for line in board:
        print(*(f"{n or '.':{numSize}} " for n in line))


def generate() -> dict:
    """
    Generates a valid Sudoku Board and then sets random cell values to
    create a Sudoku puzzle.

    returns dict{ str: list }
    """
    base = 3
    side = base * base
    rBase = range(base)
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, base * base + 1))

    solution = [[nums[pattern(r, c)] for c in cols] for r in rows]

    puzzle = copy.deepcopy(solution)

    squares = side * side
    empties = squares * 3 // 4
    for p in sample(range(squares), empties):
        puzzle[p // side][p % side] = 0

    return {"puzzle": sum(puzzle, []), "solution": sum(solution, [])}


def generate_puzzle() -> List[int]:
    """
    Generates a Sudoku Puzzle and returns it as a flat list of ints
    """
    base = 3
    side = base * base
    rBase = range(base)
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, base * base + 1))

    puzzle = [[nums[pattern(r, c)] for c in cols] for r in rows]

    squares = side * side
    empties = squares * 3 // 4
    for p in sample(range(squares), empties):
        puzzle[p // side][p % side] = 0

    return sum(puzzle, [])


def save_to_json(puzzle: dict, file_path: str) -> None:
    """Saves generated board(s) to json file"""
    with open(file_path, "w") as file:
        json.dump(puzzle, file)


def main(file_path: str = None) -> None:
    """
    Main Function:
        Generates a Board and Puzzle and
        saves them to json file
    """
    if file_path:
        save_to_json(generate(), file_path)
    else:
        file_path = Path(__file__).parent / "puzzle.json"
        save_to_json(generate(), str(file_path))


if __name__ == "__main__":
    main()
