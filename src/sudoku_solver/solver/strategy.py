# sudoku_solver.solver.strategy.py
from abc import ABC, abstractmethod


class Strategy(ABC):

    # TODO Add typehinting and docstring
    @abstractmethod
    def solve(self, board) -> None:
        ...


class BackTrack(Strategy):

    def solve(self, board) -> None:
        print("BackTrack SolutionStratagey Executed")


class BackTrackRandomStart(Strategy):

    def solve(self, board) -> None:
        print("BackTrackRandomStart SolutionStratagey Executed")


class BackTrackRandomIndex(Strategy):

    def solve(self, board) -> None:
        print("BackTrackRandomIndex SolutionStratagey Executed")


class Possibilities(Strategy):

    def solve(self, board) -> None:
        print("Possibilities SolutionStratagey Executed")
