from time import sleep
import numpy as np
from utils import load_json
from board import Board
from validate import board_not_valid

from rich import print
from rich.panel import Panel
from rich import box
from rich.live import Live
from rich.text import Text
from rich.console import Console
from rich.traceback import install

install()
console = Console()

timer = 0.25


class Board(Board):
    def update(self):
        return Panel(
            self._draw_board(),
            box=box.SIMPLE,
        )


def live_backtrack(board: Board):
    with Live(board.update(), refresh_per_second=4) as live:
        live.update(board.update())

        filled_cells = []

        for i, _ in np.ndenumerate(board.board):
            idx = i
            val = board.board[idx]
            
            sleep(timer)

            if val == 0:
                val = 1
                board.board[idx] = val
                filled_cells.insert(0, idx)
                live.update(board.update())
                
                sleep(timer)

                while board_not_valid(board):
                    if val != 9 and val < 9:
                        val += 1
                        board.board[idx] = val
                        live.update(board.update())
            
                        sleep(timer)

                    else:
                        board.board[idx] = 0
                        filled_cells.pop(0)
                        idx = filled_cells[0]
                        val = board.board[idx] + 1
                        board.board[idx] = val
                        live.update(board.update())
            
                        sleep(timer)

        live.update(board.update())


if __name__ == "__main__":
    board = Board(np.array(load_json("puzzle.json")["puzzle"]))
    live_backtrack(board)
