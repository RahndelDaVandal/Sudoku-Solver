# solver.strategy.py

import numpy as np
from abc import ABC, abstractmethod

from board import Board

from time import sleep

timer = 0.1


class Strategy(ABC):
    @abstractmethod
    def solve(self, board: np.ndarray) -> None:
        pass


class BackTrack(Strategy):
    def solve(self, board: Board) -> None:
        empty_cells = [[i, True] for i, v in np.ndenumerate(board.board) if v == 0]
        idx = 0
        val: int

        while [True for i in empty_cells if True in i]:
            val = board.get_cell(idx)
            print(
                f"TOP WHILE HAS ZEROS | idx={idx}, val={val}, cell={board.get_cell(idx)}"
            )
            sleep(timer)

            if val == 0:
                val = 1
                board.set_cell(idx, val)
                print(f"VAL == 0 | idx={idx}, val={val}, cell={board.get_cell(idx)}")
                sleep(timer)

            while board.has_violations:

                if val < 9:
                    val += 1
                    board.set_cell(idx, val)
                    print(f"VAL < 9 | idx={idx}, val={val}, cell={board.get_cell(idx)}")
                    sleep(timer)

                else:
                    val = 0
                    board.set_cell(idx, val)
                    print(
                        f"ELSE PRE BACKTRACK | idx={idx}, val={val}, cell={board.get_cell(idx)}"
                    )
                    sleep(timer)
                    idx -= 1
                    val = board.get_cell(idx)
                    print(
                        f"ELSE POST BACKTRACK | idx={idx}, val={val}, cell={board.get_cell(idx)}"
                    )
                    sleep(timer)

                    while val >= 9:
                        val = 0
                        board.set_cell(idx, val)
                        print(
                            f"ELSE WHILE PRE BACKTRACK | idx={idx}, val={val}, cell={board.get_cell(idx)}"
                        )
                        sleep(timer)
                        idx -= 1
                        val = board.get_cell(idx)
                        print(
                            f"ELSE WHILE POST BACKTRACK | idx={idx}, val={val}, cell={board.get_cell(idx)}"
                        )
                        sleep(timer)

                    val += 1
                    board.set_cell(idx, val)
                    print(
                        f"ELSE AFTER WHILE | idx={idx}, val={val}, cell={board.get_cell(idx)}"
                    )

            idx += 1
            try:
                val = board.get_cell(idx)
                print(
                    f"BOTTOM HAS_VIOLATIONS | idx={idx}, val={val}, cell={board.get_cell(idx)}"
                )
                sleep(timer)
            except Exception:
                break

        print(f"BOTTOM WHILE HAS ZEROS")
        board.show()
        print(f"\n{board.is_valid}")


class BackTrackLive(Strategy):
    def solve(self, board: np.ndarray) -> None:
        pass
