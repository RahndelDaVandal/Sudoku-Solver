from typing import List


def validate(validation_set: List[list]) -> bool:
    valid = True
    for s in validation_set:

        for value in s:
            if not 0 <= value <= 9:
                valid = False

        if len(set(s)) != len(s):
            valid = False

        print(s, valid)

    return valid
