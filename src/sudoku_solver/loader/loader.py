# sudoku_solver.loader.py
from dataclasses import dataclass, field
from . strategy import Strategy, FromSRM


@dataclass
class Loader:
    _strategy: Strategy = field(init=False, default=None)

    def __init__(self) -> None:
        if self._strategy is None:
            self._strategy = FromSRM()

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def load(self, file_path: str) -> None:
        self._strategy.load(file_path)
