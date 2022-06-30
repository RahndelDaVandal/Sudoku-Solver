from pathlib import Path
from board import Board
from utils import load_puzzle

from rich.traceback import install

from strategy import Strategy, BackTrack

install()


class Solver:
    strategy: Strategy

    def setStrategy(self, strategy: Strategy = None):
        if strategy is not None:
            self.strategy = strategy
        else:
            self.strategy = BackTrack()

    def solve(self, board: Board) -> None:
        self.strategy.solve(board)


if __name__ == "__main__":
    puzzle_path = Path(__file__).parent / "puzzle.json"
    puzzle = Board(load_puzzle(puzzle_path))

    solver = Solver()

    solver.setStrategy(BackTrack())

    solver.solve(puzzle)
