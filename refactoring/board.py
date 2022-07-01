from typing import List
from dataclasses import dataclass, field

from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich import box

from utils import load_json
from validate import validate

console = Console()


@dataclass
class Board:
    board: list
    blanks: list = field(init=False)

    def __post_init__(self) -> None:
        self.blanks = [i for i, v in enumerate(self.board) if v == 0]

    @property
    def board2d(self) -> List[list]:
        _2d = []
        start = 0
        end = 9

        for i in range(9):
            _2d.append(self.board[start:end])
            start = end
            end += 9

        return _2d

    @property
    def validation_sets(self) -> List[list]:
        validation_sets = [self.get_blocks(), self.get_cols(), self.get_rows()]
        return sum(validation_sets, [])

    @property
    def is_valid(self) -> bool:
        if self.has_blanks:
            return False
        return validate(self.validation_sets)

    @property
    def has_violations(self) -> bool:
        less_zeros = []
        for s in self.validation_sets:
            less_zeros.append([i for i in s if i != 0])
        return not validate(less_zeros)

    @property
    def has_blanks(self) -> bool:
        for blank in self.blanks:
            if self.board[blank] == 0:
                return True
        return False

    def get_blocks(self) -> List[list]:
        slices = [slice(i * 3, i * 3 + 3) for i in range(3)]

        blocks = []

        for r in slices:
            for c in slices:
                blocks.append(sum([b[c] for b in self.board2d[r]], []))

        return blocks

    def get_cols(self) -> List[list]:
        cols = []

        for c in range(len(self.board2d)):
            col = []
            for r in self.board2d:
                col.append(r[c])
            cols.append(col)

        return cols

    def get_rows(self) -> List[list]:
        return self.board2d

    def show(self) -> None:
        bg = load_json("bg.json")

        cells = [i for i, v in enumerate(bg) if v == "."]

        blanks = [v for i, v in enumerate(cells) if i in self.blanks]

        for i, v in enumerate(self.board):
            if v == 0:
                bg[cells[i]] = " "
            else:
                bg[cells[i]] = v

        text = Text()
        for idx, char in enumerate(bg):
            if idx in blanks:
                text.append(str(char), style="yellow1")
            else:
                if isinstance(char, int):
                    text.append(str(char), style="deep_sky_blue1")
                else:
                    text.append(str(char), style="grey100")

        console.print(text)

    def _show(self) -> Text:
        bg = load_json("bg.json")

        cells = [i for i, v in enumerate(bg) if v == "."]

        blanks = [v for i, v in enumerate(cells) if i in self.blanks]

        for i, v in enumerate(self.board):
            if v == 0:
                bg[cells[i]] = " "
            else:
                bg[cells[i]] = v

        text = Text()
        for idx, char in enumerate(bg):
            if idx in blanks:
                text.append(str(char), style="yellow1")
            else:
                if isinstance(char, int):
                    text.append(str(char), style="deep_sky_blue1")
                else:
                    text.append(str(char), style="grey100")
        return(text)

    def update(self):
        view = Panel(
            Text(str(self._show()), justify="center"),
            title="[bold green]Sudoku Solver",
            # subtitle="[bold green]by: Connor Sahleen",
            box=box.SIMPLE,
            # padding=2,
        )
        return Panel(view, box=box.SIMPLE, expand=True)

    def __repr__(self) -> str:
        string = ""

        for r in self.board2d:
            for c in r:
                if c == 0:
                    string += ". "
                else:
                    string += f"{c} "
            string += "\n"

        return string

    def __len__(self) -> int:
        return len(self.board)
