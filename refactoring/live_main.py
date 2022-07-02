import os
import sys
from generate import generate_puzzle
from board import Board
from solver import Solver
from strategy import BackTrackLive

if __name__ == "__main__":
    try:
        puzzle = Board(generate_puzzle())
        solver = Solver()
        solver.setStrategy(BackTrackLive())
        solver.solve(puzzle)

    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
