from rich.layout import Layout
from rich.panel import Panel
from rich import print
from rich import box

inner = Panel('HELLO WORLD', title='title', subtitle='subtitle')
outer = Panel(inner, box=box.SIMPLE, padding=5, expand=True)

print(outer)
