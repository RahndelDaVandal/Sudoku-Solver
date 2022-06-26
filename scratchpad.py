import numpy as np
from board import Board


def gen_test_board() -> np.ndarray:
    nums = [1, 2, 3]
    line = []
    board = []

    for _ in range(3):
        for _ in range(len(nums)):
            for n in nums:
                for i in range(3):
                    line.append(n)
            board.append(line)
            line = []
        nums = [i + 3 for i in nums]

    return np.array(board)


b = gen_test_board()

s = Board(b)

s.show()
