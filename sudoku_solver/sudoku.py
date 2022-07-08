# sudoku_solver.sudoku
from dataclasses import dataclass

from sudoku_solver.board import Board
from sudoku_solver.loader import Loader, FromSTR
from sudoku_solver.solver import Solver, BackTrack


# TODO - add documentation
@dataclass
class Sudoku:
    _puzzle: Board = None
    _solution: Board = None
    _loader: Loader = None
    _solver: Solver = None

    def __post_init__(self) -> None:
        if self._loader is None:
            self._loader = FromSTR()
        if self._solver is None:
            self._solver = BackTrack()

    @property
    def loader(self) -> Loader:
        return self._loader

    @loader.setter
    def loader(self, loader: Loader) -> None:
        self._loader = loader

    @property
    def solver(self) -> Solver:
        return self._solver

    @solver.setter
    def solver(self, solver: Solver) -> None:
        self._solver = solver

    @property
    def puzzle(self) -> list[int]:
        return self._puzzle

    @property
    def solution(self) -> list[int]:
        if self._solution is None:
            # TODO - Should this raise an exception?
            print("No soluiton, please run Sudoku.solve()")
        return self._solution

    def load(self, target: str) -> None:
        self._puzzle = self._loader.load(target)

    def solve(self) -> Board:
        self._solution = self._solver.solve(self._puzzle)
