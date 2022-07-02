import time

from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TextColumn,
    TimeElapsedColumn,
)

progress = Progress(
    SpinnerColumn(),
    *Progress.get_default_columns(),
    TimeElapsedColumn(),
)
task1 = progress.add_task("[red]Solving Sudoku...", total=None)

with progress:

    while not progress.finished:
        time.sleep(0.02)
