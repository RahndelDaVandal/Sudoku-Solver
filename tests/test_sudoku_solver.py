from sudoku_solver import __version__
import pytest
from sudoku_solver.solver import Solver
from sudoku_solver.strategy import Strategy, BackTrack, Possibilities
from sudoku_solver.sudoku import Sudoku


def test_version():
    assert __version__ == '0.1.0'


""" Tests for sudoku_solver.solver """


def test_should_create_Solver():
    assert Solver() is not None


def test_solver_defaults_to_BackTrack():
    solver = Solver()
    assert type(solver.strategy) == BackTrack


def test_set_strategy_to_possibilities():
    solver = Solver()
    solver.strategy = Possibilities()
    assert type(solver.strategy) == Possibilities


""" Test for sudoku_solver.sudoku """


def test_should_create_sudoku():
    assert Sudoku() is not None


def test_should_create_board_from_list_of_ints_0_to_9():
    test_board_str = "004006079000000602056092300078061030509000406020540890007410920105000000840600100"
    test_board = [int(i) for i in test_board_str]

    sudoku = Sudoku()
    sudoku.load(test_board)

    assert sudoku.board is not None and len(sudoku.board) == 81


def test_valueerror_when_board_not_type_list():
    sudoku = Sudoku()
    # when not board not type list
    test_board_str = "004006079000000602056092300078061030509000406020540890007410920105000000840600100"
    test_board = {i for i in test_board_str}

    with pytest.raises(ValueError):
        sudoku.load(test_board)


def test_valueerror_when_board_list_not_contain_ints():
    ...


def test_valueerror_when_board_contains_ints_not_in_0_to_9():
    ...
