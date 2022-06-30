import numpy as np
from board import Board
from utils import Logger

l = Logger()


def valid(slice: np.ndarray) -> bool:
    s = slice[np.nonzero(slice)].flatten()

    for i in s:
        if not isinstance(i, np.int64):
            return False
        if i > 9:
            return False
        if i < 0:
            return False

    return len(np.unique(s)) == len(s)


def validate(board: Board):
    for item in get_validation_sets(board.board):
        l(f"{type(item)} | {item}")
        if not valid(item):
            return False
    return True


def board_not_valid(board: Board):
    for item in board.test_sets:
        if not valid(item):
            return True
    return False


def get_blocks() -> list:
    indices = []
    x = [0, 3, 6]
    y = [3, 6, 9]

    for xi, xv in enumerate(x):
        row = (xv, y[xi])
        for yi, yv in enumerate(x):
            col = (yv, y[yi])
            indices.append((slice(*row), slice(*col)))

    return indices


def get_validation_sets(board: np.ndarray) -> list:
    blocks = [board[i].flatten() for i in get_blocks()]
    rows = [board[i, :] for i in range(board.shape[0])]
    cols = [board[:, i] for i in range(board.shape[1])]

    validation_set = []

    for x in [blocks, rows, cols]:
        for i in x:
            validation_set.append(i)

    return validation_set
    # return [[item for item in arr] for arr in [blocks, rows, cols]]
