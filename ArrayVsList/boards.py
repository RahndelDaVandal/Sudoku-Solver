import numpy as np
from typing import List
from dataclasses import dataclass, field
from validators import refactored_validate as Rvalidate
from validators import original_validate as Ovalidate


@dataclass
class RefactoredBoard:
    board: list
    blanks: list = field(init=False)

    def __post_init__(self) -> None:
        self.blanks = [i for i, v in enumerate(self.board) if v == 0]

    @property
    def board2d(self) -> List[list]:
        _2d = []
        start = 0
        end = 9

        for i in range(9):
            _2d.append(self.board[start:end])
            start = end
            end += 9

        return _2d

    @property
    def validation_sets(self) -> List[list]:
        validation_sets = [self.get_blocks(), self.get_cols(), self.get_rows()]
        return sum(validation_sets, [])

    @property
    def is_valid(self) -> bool:
        if self.has_blanks:
            return False
        return Rvalidate(self.validation_sets)

    @property
    def has_violations(self) -> bool:
        less_zeros = []
        for s in self.validation_sets:
            less_zeros.append([i for i in s if i != 0])
        return not Rvalidate(less_zeros)

    @property
    def has_blanks(self) -> bool:
        for blank in self.blanks:
            if self.board[blank] == 0:
                return True
        return False

    def get_blocks(self) -> List[list]:
        slices = [slice(i * 3, i * 3 + 3) for i in range(3)]

        blocks = []

        for r in slices:
            for c in slices:
                blocks.append(sum([b[c] for b in self.board2d[r]], []))

        return blocks

    def get_cols(self) -> List[list]:
        cols = []

        for c in range(len(self.board2d)):
            col = []
            for r in self.board2d:
                col.append(r[c])
            cols.append(col)

        return cols

    def get_rows(self) -> List[list]:
        return self.board2d

    def __repr__(self) -> str:
        string = ""

        for r in self.board2d:
            for c in r:
                if c == 0:
                    string += ". "
                else:
                    string += f"{c} "
            string += "\n"

        return string


@dataclass
class OriginalBoard:
    board: np.ndarray

    def _block_indices(self) -> list:
        indices = []
        x = [0, 3, 6]
        y = [3, 6, 9]

        for xi, xv in enumerate(x):
            row = (xv, y[xi])
            for yi, yv in enumerate(x):
                col = (yv, y[yi])
                indices.append((slice(*row), slice(*col)))

        return indices

    @property
    def test_sets(self) -> list:
        v_set = []

        blocks = [self.board[i].flatten() for i in self._block_indices()]
        rows = [self.board[i, :] for i in range(self.board.shape[0])]
        cols = [self.board[:, i] for i in range(self.board.shape[1])]

        for item in [blocks, rows, cols]:
            [v_set.append(i) for i in item]

        return v_set

    @property
    def is_valid(self) -> bool:
        return Ovalidate(self.test_sets)

    def __repr__(self) -> str:
        string = ""

        for r in self.board:
            for c in r:
                if c == 0:
                    string += ". "
                else:
                    string += f"{c} "
            string += "\n"

        return string
