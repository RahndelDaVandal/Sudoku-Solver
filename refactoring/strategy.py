from abc import ABC, abstractmethod
from board import Board

from rich.live import Live
from rich.console import Console
from rich.traceback import install

install()
console = Console

from utils import Logger
l = Logger()


class Strategy(ABC):

    @abstractmethod
    def solve(self, board: Board) -> None:
        pass


class BackTrack(Strategy):

    def solve(self, board: Board) -> None:
        ...


class BackTrackLive(Strategy):

    def solve(self, board: Board) -> None:
        # l(f'{board.validation_sets}')
        # l(f'{board}\n')
        with Live(board.update(), refresh_per_second=10, screen=True) as live:
            
            idx = 0
            blanks = board.blanks
            _board = board.board

            # l(f'has_blanks={board.has_blanks}')

            while board.has_blanks:
                live.update(board.update())
                val = _board[blanks[idx]]
                # l(f'TOP WHILE HAS BLANKS | idx={idx}, val={val}, blanks_val={blanks[idx]}')
                if val == 0:
                    # l(f'IF VAL == 0 | idx={idx}, val={val}, blanks_val={blanks[idx]} board_val={board.board[blanks[idx]]}')
                    val = 1
                    _board[blanks[idx]] = val
                    live.update(board.update())

                # l(f'BEFORE WHILE VIOLATIONS | idx={idx}, val={val}, blanks_val={blanks[idx]}')
                # l(f'has_violations={board.has_violations}')
                while board.has_violations:
                    # l(f'TOP WHILE VIOLATIONS | idx={idx}, val={val}, blanks_val={blanks[idx]}')
                    # l(f'has_violations={board.has_violations}')
                    if val < 9:
                        val += 1
                        _board[blanks[idx]] = val
                        live.update(board.update())
                        # l(f'END VAL < 9 | idx={idx}, val={val}, blanks_val={blanks[idx]} board_val={board.board[blanks[idx]]}')
                    if val >= 9 and idx != 0:
                        val = 0
                        _board[blanks[idx]] = val
                        idx -= 1
                        val = _board[blanks[idx]]
                        live.update(board.update())
                        # l(f'END VAL > 9 BEFORE WHILE | idx={idx}, val={val}, blanks_val={blanks[idx]} board_val={board.board[blanks[idx]]}')
                        while val >= 9:
                            # l(f'TOP WHILE VAL > 9 | idx={idx}, val={val}, blanks_val={blanks[idx]}')
                            val = 0
                            _board[blanks[idx]] = val
                            idx -= 1
                            val = _board[blanks[idx]]
                            live.update(board.update())
                            # l(f'BOTTOM WHILE VAL > 9 | idx={idx}, val={val}, blanks_val={blanks[idx]} board_val={board.board[blanks[idx]]}')
                        val += 1
                        _board[blanks[idx]] = val
                        live.update(board.update())
                    # l(f'BOTTOM WHILE VIOLATIONS | idx={idx}, val={val}, blanks_val={blanks[idx]} board_val={board.board[blanks[idx]]}')

                try:
                    idx += 1
                    val = _board[blanks[idx]]
                    # l(f'BOTTOM WHILE has_blanks | idx={idx}, val={val}, blanks_val={blanks[idx]} board_val={board.board[blanks[idx]]}')
                except Exception as e:
                    pass
                live.update(board.update())
                # l(f'{board}\n')
