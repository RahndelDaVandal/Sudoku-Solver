# sudoku_solver.solver
from abc import ABC, abstractmethod
from dataclasses import dataclass

from sudoku_solver.board import Board


# TODO - add documentation
@dataclass
class Solver(ABC):
    @staticmethod
    def board_is_valid(board: list[int]) -> bool:
        # TODO - add function code
        ...

    @staticmethod
    def board_has_violatons(board: list[int]) -> bool:
        # TODO - add function code
        ...

    @abstractmethod
    def solve(self, board: Board) -> list[int]:
        pass


# TODO - add documentation
@dataclass  # TODO - Not sure if dataclass decorator gets inherited
class BackTrack(Solver):
    idx: int = None

    def solve(self, board: Board) -> list[int]:
        print("BackTrack Solver Executed")
