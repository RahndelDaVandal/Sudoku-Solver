from typing import List


def validate(validation_set: List[list]) -> bool:
    for s in validation_set:

        for value in s:
            if not 0 <= value <= 9:
                return False

        if len(set(s)) != len(s):
            return False
    return True
