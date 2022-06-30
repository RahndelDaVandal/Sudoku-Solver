import json
from time import sleep
import numpy as np
from utils import load_json, Logger
from board import Board
from validate import board_not_valid, validate

from rich import print
from rich.panel import Panel
from rich import box
from rich.live import Live
from rich.text import Text
from rich.console import Console
from rich.traceback import install

install()
console = Console()


l = Logger()


def verify_solution(board: Board) -> bool:
    l("---------------------------------------------------")
    l("              VERIFYING SOLVED PUZZLE")
    l("---------------------------------------------------")
    is_valid = validate(board)
    l(f"PUZZLE is_valid = {is_valid}\n")
    l("---------------------------------------------------")


def verify_against_original_solution(puzzle: np.ndarray, solution: np.ndarray) -> bool:
    does_match = True
    l("---------------------------------------------------")
    l("  VERIFY SOLVED PUZZLE AGAINST ORIGINAL SOLUTION")
    l("---------------------------------------------------")
    for idx, val in np.ndenumerate(puzzle):
        if puzzle[idx] != solution[idx]:
            l(
                f"puzzle[{idx}] = {puzzle[idx]} | solution[{idx}] = {solution[idx]} | {puzzle[idx] == solution[idx]}"
            )
            does_match = False
        l(
            f"puzzle[{idx}] = {puzzle[idx]} | solution[{idx}] = {solution[idx]} | {puzzle[idx] == solution[idx]}"
        )
    l("---------------------------------------------------")
    l(f"PUZZLE DOES MATCH ORIGINAL SOLUTION = {does_match}")
    l("---------------------------------------------------")
    return does_match


class Board(Board):
    def update(self):

        view = Panel(
            Text(str(self._draw_board()), justify="center"),
            title="[bold green]Sudoku Solver",
            # subtitle="[bold green]by: Connor Sahleen",
            box=box.SIMPLE,
            # padding=2,
        )
        return Panel(view, box=box.SIMPLE, expand=True)

    def _draw_board(self) -> str:
        with open("bg.json", "r") as file:
            bg = json.load(file)

        cells = [i for i, v in enumerate(bg) if v == "."]

        for i, n in enumerate(self.board.flatten()):
            if n == 0:
                bg[cells[i]] = " "
            else:
                bg[cells[i]] = str(n)

        return "".join(bg)


def live_backtrack(board: Board):
    empty_cells = [[i, True] for i, v in np.ndenumerate(board.board) if v == 0]
    idx = 0

    with Live(board.update(), refresh_per_second=10, screen=True) as live:
        live.update(board.update())

        while [True for i in empty_cells if True in i]:
            live.update(board.update())

            c = empty_cells[idx]
            val = board.board[c[0]]

            if val == 0:
                val = 1
                board.board[c[0]] = val
                live.update(board.update())

            while board_not_valid(board):
                if val != 9 or val < 9:
                    val += 1
                    board.board[c[0]] = val
                    live.update(board.update())

                else:
                    val = 0
                    board.board[c[0]] = val
                    c[1] = True
                    idx -= 1
                    c = empty_cells[idx]
                    val = board.board[c[0]]

                    while val >= 9:
                        val = 0
                        board.board[c[0]] = val
                        c[1] = True
                        idx -= 1
                        c = empty_cells[idx]
                        val = board.board[c[0]]

                    val += 1
                    board.board[c[0]] = val

                    live.update(board.update())

            c[1] = False
            idx += 1
            if idx > (len(empty_cells) - 1):
                break
            else:
                c = empty_cells[idx]

            live.update(board.update())

    live.update(board.update())


if __name__ == "__main__":
    puzzle = Board(np.array(load_json("puzzle.json")["puzzle"]))
    solution = Board(np.array(load_json("puzzle.json")["solution"]))
    live_backtrack(puzzle)

    puzzle.show()

    valid = validate(puzzle)

    if valid:
        print(f"\nSolution is valid!")
    else:
        print(f"Solution not valid!")
