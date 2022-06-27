import json
import numpy as np
from pathlib import Path
from typing import List
from dataclasses import dataclass, field


def generate_block_names(prefix: str = "block", num_block: int = 9) -> list:
    return [(prefix + str(i)) for i, _ in enumerate(range(num_block), start=1)]


def generate_block_indices() -> list:
    indices = []
    x = [0, 3, 6]
    y = [3, 6, 9]

    for xi, xv in enumerate(x):
        row = (xv, y[xi])
        for yi, yv in enumerate(x):
            col = (yv, y[yi])
            indices.append((row, col))

    return indices


def generate_blocks(names: List[str] = None, indices: List[tuple] = None) -> list:
    if not names:
        names = generate_block_names()
    if not indices:
        indices = generate_block_indices()

    blocks = []

    for idx, val in enumerate(names):
        blocks.append(Block(val, *indices[idx]))

    return blocks


@dataclass
class Block:
    name: str
    row: tuple
    col: tuple

    def __repr__(self) -> str:
        row_str = f"{self.row[0]}:{self.row[1]}"
        col_str = f"{self.col[0]}:{self.col[1]}"
        return f"{self.name} = [{row_str}, {col_str}]"

    @property
    def idx(self) -> tuple:
        return (slice(*self.row), slice(*self.col))


@dataclass
class Board:
    arr: np.ndarray
    blocks: List[Block] = field(default_factory=generate_blocks)
    rows: list = None
    cols: list = None

    def __post_init__(self) -> None:
        self.rows = self.get_rows()
        self.cols = self.get_cols()

    def __repr__(self) -> str:
        self.show()

    def get_block(self, index: int) -> np.ndarray:
        return self.arr[self.blocks[index].idx]

    def get_blocks(self) -> list:
        return [self.get_block(i) for i, _ in enumerate(self.blocks)]

    def get_rows(self) -> list:
        return [self.arr[i, :] for i, _ in enumerate(range(self.arr.shape[0]))]

    def get_cols(self) -> list:
        return [self.arr[:, i] for i, _ in enumerate(range(self.arr.shape[0]))]

    def get_validation_set(self) -> list:
        v_set = []

        for i in self.get_blocks():
            v_set.append(i)

        for i in self.get_rows():
            v_set.append(i)

        for i in self.get_cols():
            v_set.append(i)

        return v_set

    def _load_bg(self) -> list:
        bg_file = Path(__file__).parent / "bg.json"
        if not bg_file.is_file():
            print('ERROR - File "bg.json" Not Found')
            return
        with open(str(bg_file), "r") as file:
            return json.load(file)

    def show(self):
        bg = self._load_bg()

        cells = [i for i, v in enumerate(bg) if v == "."]

        for i, n in enumerate(self.arr.flatten()):
            if n == 0:
                bg[cells[i]] = " "
            else:
                bg[cells[i]] = str(n)

        print("".join(bg))
        return "".join(bg)
