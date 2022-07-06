# sudoku_solver.loader
from abc import ABC, abstractmethod


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
