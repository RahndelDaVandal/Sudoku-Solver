from rich.console import Console
from rich.table import Table
from rich import box


table = Table(
    title="Sudoku-Solver", show_header=False, box=box.DOUBLE_EDGE, border_style="-"
)

table.add_column("")
table.add_column("")
table.add_column("")

table.add_row("1", "2", "3")
table.add_row("4", "5", "6")
table.add_row("7", "8", "9")

console = Console()
console.print(table)
