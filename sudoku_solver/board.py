# sudoku_solver.board
from dataclasses import dataclass


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
