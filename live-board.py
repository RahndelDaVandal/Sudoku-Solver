import json
import numpy as np
from rboard import Board

from rich import print
from rich.panel import Panel
from rich import box
from rich.live import Live
from rich.text import Text
from rich.console import Console
from rich.traceback import install

install()
console = Console()

if __name__ == "__main__":
    with open("puzzle.json", "r") as file:
        p = Board(np.array(json.load(file)["puzzle"]))

    print(p.test_sets)
