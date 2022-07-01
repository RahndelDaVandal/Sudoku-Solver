import json
import copy
from pathlib import Path

# randomize rows, columns and numbers (of valid base pattern)
from random import sample


# pattern for a baseline valid solution
def pattern(r, c):
    return (base * (r % base) + r // base + c) % side


def shuffle(s):
    return sample(s, len(s))


base = 3
side = base * base


def gen_solution() -> list:
    rBase = range(base)
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, base * base + 1))
    return [[nums[pattern(r, c)] for c in cols] for r in rows]


def gen_puzzle(solution_board: list) -> list:
    puzzle = copy.deepcopy(solution_board)
    squares = side * side
    empties = squares * 3 // 4
    for p in sample(range(squares), empties):
        puzzle[p // side][p % side] = 0
    return puzzle


def display(board: list) -> None:
    numSize = len(str(side))
    for line in board:
        print(*(f"{n or '.':{numSize}} " for n in line))


def generate() -> dict:
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


def save_to_json(puzzle: dict, file_path: str) -> None:
    with open(file_path, "w") as file:
        json.dump(puzzle, file)


def main(file_path: str = None) -> None:
    if file_path:
        save_to_json(generate(), file_path)
    else:
        file_path = Path(__file__).parent / "puzzle.json"
        save_to_json(generate(), str(file_path))


if __name__ == "__main__":
    main()
