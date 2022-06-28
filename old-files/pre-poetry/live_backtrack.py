import json
from time import sleep
import numpy as np
from utils import load_json, Logger
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

l = Logger()
timer = 0


def verify_solution(puzzle: np.ndarray, solution: np.ndarray) -> bool:
    l('---------------------------------------------------')
    l('VERIFY SOLVED PUZZLE AGAINST SOLUTION')
    l('---------------------------------------------------')
    for idx, val in np.ndenumerate(puzzle):
        l(f'puzzle[{idx}] = {puzzle[idx]} | solution[{idx}] = {solution[idx]} | {puzzle[idx] == solution[idx]}')
        if puzzle[idx] != solution[idx]:
            return False
        return True


class Board(Board):
    def update(self):

        view = Panel(
            Text(str(self._draw_board()), justify='center'),
            title="[bold green]Sudoku Solver",
            subtitle="[bold green]by: Connor Sahleen",
            box=box.SIMPLE,
            # padding=2,
        )
        return Panel(view, box=box.SIMPLE, expand=True)

    def _draw_board(self) -> str:
        with open("bg.json", "r") as file:
            bg = json.load(file)

        rtext = Text()

        cells = [i for i, v in enumerate(bg) if v == "."]

        for i, n in enumerate(self.board.flatten()):
            if n == 0:
                bg[cells[i]] = " "
            else:
                bg[cells[i]] = str(n)

        for i, v in enumerate(bg):
            if i in cells:
                rtext.append(v, style='bold green')
            else: 
                rtext.append(v)

        return rtext
        # return "".join(bg)
        # return "".join([str(i) for i in bg])


def live_backtrack(board: Board):
    empty_cells = [[i, True] for i, v in np.ndenumerate(board.board) if v == 0]
    idx = 0

    l(f'empty_cells = {empty_cells}')
    l(f"idx = {idx}")

    with Live(board.update(), refresh_per_second=10, screen=True) as live:
        live.update(board.update())

        while [True for i in empty_cells if True in i]:
            l(f'TOP OF WHILE LOOP {len([True for i in empty_cells if True in i])}')
            live.update(board.update())
            c = empty_cells[idx]

            val = board.board[c[0]]
            
            l(f'START OF OUTER WHILE ({c}, {val}) idx={idx}')

            if val == 0:
                val = 1
                board.board[c[0]] = val
                live.update(board.update())
                l(f'IF VAL == 0 ({c}, {val})')

            while board_not_valid(board):
                if val != 9 or val < 9:
                    val += 1
                    board.board[c[0]] = val
                    live.update(board.update())

                    l(f'WHILE NOT VALID IF VAL != or < 9 ({c}, {val})')
                    sleep(timer)

                else:
                    l(f'WHILE NOT VALID - ELSE - CURRENT CELL ({c}, {val}) idx={idx}')
                    val = 0
                    board.board[c[0]] = val
                    c[1] = True
                    idx -= 1
                    c = empty_cells[idx]
                    val = board.board[c[0]]

                    while val >= 9:
                        l(f'WHILE NOT VALID - ELSE - WHILE >= 9 TOP ({c}, {val}) idx={idx}')
                        val = 0
                        board.board[c[0]] = val
                        c[1] = True
                        idx -= 1
                        c = empty_cells[idx]
                        val = board.board[c[0]]
                        l(f'WHILE NOT VALID - ELSE - WHILE >= 9 BOTTOM ({c}, {val}) idx={idx}')
                    
                    val += 1
                    board.board[c[0]] = val

                    live.update(board.update())

                    l(f'WHILE NOT VALID - ELSE - PREVIOUS CELL ({c}, {val}) idx={idx}')
                    sleep(timer)

            c[1] = False
            l(f'AFTER WHILE VALID (OLD CELL) ({c}, {val}) idx={idx}')
            idx += 1
            if idx > (len(empty_cells) - 1):
                break
            else:
                c = empty_cells[idx]
            l(f'AFTER WHILE VALID (NEW CELL) ({c}, {val}) idx={idx}')

            live.update(board.update())
            sleep(timer)

    live.update(board.update())

    l(f"\n\nFinal Valid check. board_not_valid = {board_not_valid(board)}")


if __name__ == "__main__":
    puzzle = Board(np.array(load_json("puzzle.json")["puzzle"]))
    solution = Board(np.array(load_json("puzzle.json")["solution"]))
    live_backtrack(puzzle)

    puzzle.show()

