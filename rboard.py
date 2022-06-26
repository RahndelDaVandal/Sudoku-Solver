import json
import numpy as np
from dataclasses import dataclass


@dataclass
class Board:
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

    @property
    def show(self) -> str:
        return self._draw_board()

    def __repr__(self) -> str:
        return self._draw_board()
