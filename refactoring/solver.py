from board import Board
from strategy import Strategy, BackTrack


class Solver:
    strategy: Strategy

    def setStrategy(self, strategy: Strategy = None):
        if strategy is not None:
            self.strategy = strategy
        else:
            self.strategy = BackTrack()

    def solve(self, board: Board) -> None:
        self.strategy.solve(board)
