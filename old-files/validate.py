import numpy as np
from board import Board


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
    for item in board.test_sets:
        if not valid(item):
            return False
    return True


def board_not_valid(board: Board):
    for item in board.test_sets:
        if not valid(item):
            return True
    return False
