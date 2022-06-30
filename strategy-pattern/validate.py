import numpy as np


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


def valid_check(slice: np.ndarray) -> bool:
    s = slice[np.nonzero(slice)].flatten()

    for cell in s:
        if not isinstance(cell, np.int64):
            return False
        if cell > 9:
            return False
        if cell < 0:
            return False

    return len(np.unique(s)) == len(s)


def validate(board: np.ndarray):
    for item in get_validation_sets(board):
        if not valid_check(item):
            return False
    return True
