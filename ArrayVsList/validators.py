import numpy as np
from typing import List


def refactored_validate(validation_set: List[list]) -> bool:
    for s in validation_set:

        for value in s:
            if not 0 <= value <= 9:
                return False

        if len(set(s)) != len(s):
            return False
    return True


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


def original_validate(validation_set: List[np.ndarray]) -> bool:
    for item in validation_set:
        if not valid(item):
            return False
    return True
