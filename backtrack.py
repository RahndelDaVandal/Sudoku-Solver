from time import sleep
import numpy as np
from utils import load_json
from board import Board
from validate import board_not_valid

from rich.console import Console
from rich.traceback import install

install()
console = Console()

timer = 0.25


def backtrack(board: Board) -> None:
    filled_cells = []
    # board.update()
    board.show()

    for i, _ in np.ndenumerate(board.board):
        idx = i
        val = board.board[idx]
        print(f"idx({idx}), val({val})")
        sleep(timer)

        if val == 0:
            val = 1
            board.board[idx] = val
            filled_cells.insert(0, idx)
            print("EMPTY CELL FOUND")
            print(f"idx({idx}), val({val})")
            sleep(timer)

            while board_not_valid(board):
                if val != 9 and val < 9:
                    val += 1
                    board.board[idx] = val
                    print(f"idx({idx}), val({val})")
                    sleep(timer)
                else:
                    print("BACKTRACKING")
                    print(f"len(filled_cells) = {len(filled_cells)}")
                    board.board[idx] = 0
                    filled_cells.pop(0)
                    print(f"len(filled_cells) = {len(filled_cells)}")
                    idx = filled_cells[0]
                    val = board.board[idx] + 1
                    board.board[idx] = val
                    print(f"idx({idx}), val({val})")
                    sleep(timer)
    board.show()


if __name__ == "__main__":
    puzzle = Board(np.array(load_json("puzzle.json")["puzzle"]))
    solution = Board(np.array(load_json("puzzle.json")["solution"]))

    backtrack(puzzle)
