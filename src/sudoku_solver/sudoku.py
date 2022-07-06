# sudoku_solver.sudoku.py
from pathlib import Path
from dataclasses import dataclass, field


@dataclass
class Sudoku:
    board: list[int] = field(init=False)
    empties: list[int] = field(init=False)

    def load(self, board: list[int]) -> None:
        if not self._load_validator(board):
            return
        self.board = board

    def load_from_file(self, file_path: str) -> None:
        if not Path(file_path).is_file():
            raise FileNotFoundError
        with open(file_path, "r") as file:
            board = file.readline()

        if not self._load_validator(board):
            return

        self.board = board

    def _load_validator(self, board: list[int]) -> bool:
        if not isinstance(board, list):
            raise ValueError("Invalid Value for Board. Must be type list[int]")

        for item in board:
            if not isinstance(item, int):
                raise ValueError(
                    "Invalid Value in Board. All items in list must be type int"
                )
            if item < 0 or item > 9:
                raise ValueError(
                    "Invalid Value in Board. All items in list must be int 0-9"
                )

        return True

    def _display_str(self) -> str:
        ...

    def __repr__(self) -> str:
        ...
