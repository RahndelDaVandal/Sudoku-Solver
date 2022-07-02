from abc import ABC, abstractmethod
from board import Board

from rich.live import Live
from rich.traceback import install
from rich.console import Console

install()


class Strategy(ABC):
    @abstractmethod
    def solve(self, board: Board) -> None:
        pass


class BackTrack(Strategy):
    def solve(self, board: Board) -> None:
        console = Console()
        idx = 0

        while board.has_blanks:
            val = board.board[board.blanks[idx]]

            if val == 0:
                val = 1
                board.board[board.blanks[idx]] = val

            while board.has_violations:
                while val >= 9:

                    val = 0
                    board.board[board.blanks[idx]] = val
                    idx -= 1
                    val = board.board[board.blanks[idx]]

                val += 1
                board.board[board.blanks[idx]] = val

            try:
                idx += 1
                val = board.board[board.blanks[idx]]
            except Exception:
                pass

        console.print(board.update())


class BackTrackLive(Strategy):
    def solve(self, board: Board) -> None:
        console = Console()

        with Live(
            board.update(), console=console, refresh_per_second=10, screen=True
        ) as live:
            idx = 0

            while board.has_blanks:
                val = board.board[board.blanks[idx]]
                # live.update(board.update())

                if val == 0:
                    val = 1
                    board.board[board.blanks[idx]] = val

                while board.has_violations:
                    while val >= 9:

                        val = 0
                        board.board[board.blanks[idx]] = val
                        idx -= 1
                        val = board.board[board.blanks[idx]]

                    val += 1
                    board.board[board.blanks[idx]] = val

                try:
                    idx += 1
                    val = board.board[board.blanks[idx]]
                    live.update(board.update())
                except Exception:
                    pass

        console.print(board.update())
