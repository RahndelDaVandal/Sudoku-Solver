# sudokusolver.solver.solver.py
from dataclasses import dataclass, field
from .strategy import Strategy, BackTrack


@dataclass
class Solver:
    _strategy: Strategy = field(init=False, default=None)

    def __post_init__(self) -> None:
        if self._strategy is None:
            self._strategy = BackTrack()

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    # TODO type hint for board
    def solve(self, board) -> None:
        self._strategy.solve(board)
