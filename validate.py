import numpy as np
from board import Board


def valid(slice: np.ndarray) -> bool:
    s = slice.flatten()

    for i in s:
        if not isinstance(i, np.int64):
            return False
        if i > 9:
            return False
        if i < 0:
            return False

    return len(np.unique(s)) == len(s)


def validate(board: Board):
    for item in board.get_validation_set():
        if not valid(item):
            return False
    return True
