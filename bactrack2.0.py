import numpy as np


from utils import Logger, json_file_to_np
from board import Board
from validate import board_not_valid


def live_backtrack(board: Board):
    empty_cells = [[i, True] for i, v in np.ndenumerate(board.board) if v == 0]
    idx = 0

    while [True for i in empty_cells if True in i]:
        c = empty_cells[idx]
        val = board.board[c[0]]

        if val == 0:
            val = 1
            board.board[c[0]] = val

        while board_not_valid(board):
            if val != 9 or val < 9:
                val += 1
                board.board[c[0]] = val

            else:
                val = 0
                board.board[c[0]] = val
                c[1] = True
                idx -= 1
                c = empty_cells[idx]
                val = board.board[c[0]]

                while val >= 9:
                    val = 0
                    board.board[c[0]] = val
                    c[1] = True
                    idx -= 1
                    c = empty_cells[idx]
                    val = board.board[c[0]]

                val += 1
                board.board[c[0]] = val

        c[1] = False
        idx += 1
        if idx > (len(empty_cells) - 1):
            break
        else:
            c = empty_cells[idx]


def backtrack(board: Board) -> None:
    idx = 0

    while board_not_valid(board):
        while [True for i, v in np.ndenumerate(board.board) if v == 0]:
            val = board.board[idx]

            if val == 0:
                val = 1
                board.board[idx] = val

            if val != 9 or val <= 9:
                val += 1
                board.board[idx] = val
            else:
                # backtrack
                ...
                while val >= 9:
                    # backtrack till not >= 9
                    ...

            idx += 1


if __name__ == "__main__":
    ...
