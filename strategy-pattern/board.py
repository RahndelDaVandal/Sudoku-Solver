import json
import numpy as np
from dataclasses import dataclass, field
from validate import validate


@dataclass
class Board:
    board: np.ndarray
    index: list = field(init=False, repr=False)

    def __post_init__(self) -> None:
        nums = np.arange(0, 9)
        self.index = [(r, c) for c in nums for r in nums]

    @property
    def is_valid(self) -> bool:
        if [True for _, value in np.ndenumerate(self.board) if value == 0]:
            return False
        return validate(self.board)

    @property
    def has_violations(self) -> bool:
        return not validate(self.board)

    def get_cell(self, index: int) -> int:
        return self.board[self.index[index]]

    def set_cell(self, index: int, value: int) -> None:
        self.board[self.index[index]] = value

    def _draw_board(self) -> str:
        with open("bg.json", "r") as file:
            bg = json.load(file)

        cells = [i for i, v in enumerate(bg) if v == "."]

        for i, n in enumerate(self.board.flatten()):
            if n == 0:
                bg[cells[i]] = " "
            else:
                bg[cells[i]] = str(n)

        return "".join(bg)

    def show(self) -> str:
        print(self._draw_board())

    def __repr__(self) -> str:
        return self._draw_board()
