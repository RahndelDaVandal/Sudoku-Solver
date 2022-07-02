from timeit import timeit

normal_setup = """
from solver import Solver
from strategy import BackTrackLive
from board import Board
from utils import load_json
"""
normal_stmt = """
puzzle = Board(load_json('puzzle.json')['puzzle'])
solver = Solver()
solver.setStrategy()
solver.solve(puzzle)
"""
normal_time = timeit(setup=normal_setup, stmt=normal_stmt, number=1)
print(f"BackTrack completed in {normal_time:.4f}\n")

live_setup = """
from solver import Solver
from strategy import BackTrackLive
from board import Board
from utils import load_json
"""
live_stmt = """
puzzle = Board(load_json('puzzle.json')['puzzle'])
solver = Solver()
solver.setStrategy(BackTrackLive())
solver.solve(puzzle)
"""
live_time = timeit(setup=live_setup, stmt=live_stmt, number=1)
print(f"BackTrackLive completed in {live_time:.4f}\n")
