import os
import sys
from generate import generate_puzzle
from board import Board
from solver import Solver
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TextColumn,
    TimeElapsedColumn,
)


if __name__ == "__main__":
    try:
        progress = Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TimeElapsedColumn(),
        )
        task1 = progress.add_task("[bold cyan]Solving Sudoku...", total=None)
        with progress:
            sudoku = Board(generate_puzzle())
            solver = Solver()
            solver.setStrategy()
            solver.solve(sudoku)

    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
