from solver import Solver
from strategy import BackTrackLive
from board import Board
from utils import load_json

if __name__ == "__main__":
    puzzle = Board(load_json('puzzle.json')['puzzle'])
    solver = Solver()
    solver.setStrategy(BackTrackLive())
    solver.solve(puzzle)
