from typing import List
from dataclasses import dataclass, field
from validate import validate


@dataclass
class Board:
    board: list
    blanks: list = field(init=False)

    def __post_init__(self) -> None:
        self.blanks = [idx for idx, val in enumerate(self.board) if val == 0]

    @property
    def validation_sets(self) -> List[list]:
        validation_sets = [self._get_blocks(), self._get_cols(), self._get_rows()]
        return sum(validation_sets, [])

    @property
    def is_valid(self) -> bool:
        if self.has_blanks:
            return False
        return validate(self.validation_sets)

    @property
    def has_violations(self) -> bool:
        return validate(self.validation_sets)

    @property
    def has_blanks(self) -> bool:
        for blank in self.blanks:
            if self.board[blank] == 0:
                return True
        return False

    def _get_blocks(self) -> List[list]:
        slices = [slice(i * 3, i * 3 + 3) for i in range(3)]

        blocks = []

        for r in slices:
            for c in slices:
                blocks.append(sum([b[c] for b in self.board[r]], []))

        return blocks

    def _get_cols(self) -> List[list]:
        cols = []

        for c in range(len(test)):
            col = []
            for r in self.board:
                col.append(r[c])
            cols.append(col)

        return cols

    def _get_rows(self) -> List[list]:
        return self.board

    def _draw_board(self) -> str:
        ...

    def show(self) -> None:
        print(self._draw_board())

    def __repr__(self) -> str:
        return self._draw_board()
