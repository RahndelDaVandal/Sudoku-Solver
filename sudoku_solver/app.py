# sudokusolver.app.py
from sudoku_solver.solver import Solver
from sudoku_solver.strategy import BackTrack, Strategy
from sudoku_solver.sudoku import Sudoku


solver = Solver()

print(type(solver.strategy))

print(type(solver.strategy) == BackTrack)

sudoku = Sudoku()


test_board_str = (
    "004006079000000602056092300078061030509000406020540890007410920105000000840600100"
)
test_board = [int(i) for i in test_board_str]

print(test_board)
print(type(test_board), type(test_board[0]))
print(len(test_board))

sudoku.load(test_board)
