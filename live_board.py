from time import sleep
import numpy as np
from utils import load_json
from board import Board

from rich import print
from rich.panel import Panel
from rich import box
from rich.live import Live
from rich.text import Text
from rich.console import Console
from rich.traceback import install

install()
console = Console()


class Board(Board):
    def update(self):
        return Panel(
                self._draw_board(),
                box=box.SIMPLE,
                )


if __name__ == "__main__":
    board = Board(np.array(load_json('puzzle.json')['puzzle']))

    with Live(board.update(), refresh_per_second=4) as live:
        for i in range(0, 10):
            sleep(0.5)
            board.board[0, 0] = i
            live.update(board.update())
