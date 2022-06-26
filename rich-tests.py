from time import sleep
import json
import numpy as np
from pathlib import Path
from rich import print
from rich.panel import Panel
from rich import box
from rich.live import Live
from rich.text import Text


def load_bg() -> list:
    bg_file = Path(__file__).parent / "bg.json"
    if not bg_file.is_file():
        print('ERROR - File "bg.json" Not Found')
        return
    with open(str(bg_file), "r") as file:
        return json.load(file)


def show(arr: np.ndarray):
    bg = load_bg()

    cells = [i for i, v in enumerate(bg) if v == "."]

    for i, n in enumerate(arr.flatten()):
        if n == 0:
            bg[cells[i]] = " "
        else:
            bg[cells[i]] = str(n)

    return Text("".join(bg), justify="center")


with open("puzzle.json", "r") as file:
    arr = np.array(json.load(file)["puzzle"])

# print(Panel.fit(show(arr), box=box.SIMPLE))


def live_board() -> None:
    return Panel(
        show(arr),
        box=box.SIMPLE,
    )


if __name__ == "__main__":
    with Live(live_board(), refresh_per_second=4) as live:
        for i in range(0, 10):
            sleep(0.5)
            arr[0, 0] = i
            live.update(live_board())
