from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path


# TODO - add documentation
@dataclass
class Board:
    _board: list[int] = None
    _blanks: list[int] = None

    @property
    def board(self) -> list[int]:
        return self._board

    @board.setter
    def board(self, board: list[int]) -> None:
        # TODO Validate the loaded board here? or in loader?
        self._blanks = [i for i, v in enumerate(board) if v == 0]
        self._board = board


# TODO - add documentation
class Loader(ABC):
    @staticmethod
    def _is_valid(board: list[int]) -> bool:
        if not isinstance(board, list):
            raise ValueError("must be type list (list[int])")
        if len(board) != 80:
            raise ValueError("list must have a length of 81")
        for i in board:
            if not isinstance(i, int):
                raise ValueError("list must contain only ints")
            if i < 0 or i > 9:
                raise ValueError("list must contain ints between 0 to 9")

    @abstractmethod
    def load(self, target: str) -> list[int]:
        pass


# TODO - add documentation
class FromSTR(Loader):
    def load(self, target: str) -> list[int]:
        board = target.split()

        for item in board:
            if not isinstance(item, int):
                # TODO - I don't think this would ever be raised because of
                # inherited validation. Overload? or refactor validation
                # out of the Loader class?
                raise ValueError('invalid format, must be "0123456789"')

        if not self._is_valid(board):
            return
        return board


# TODO - add documentation
# TODO - sdm files usually contain mutlipule sudokus which would break the code
class FromSDM(Loader):
    def load(self, target: str) -> list[int]:
        file_path = Path(target)

        if not file_path.is_file():
            raise FileExistsError(f"{file_path.name} does not exist")
        if file_path.stem != ".sdm":
            raise ValueError(f"{file_path.name} is not a .sdm file")

        with open(str(file_path), "r") as file:
            # TODO - Add .sdm parsing code
            board = file

        print("FromSDM Loader Executed")
        if not self._is_valid(board):
            return
        return board


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
