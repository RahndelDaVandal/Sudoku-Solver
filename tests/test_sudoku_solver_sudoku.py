# test_sudoku_solver_sudoku.py

import pytest
from sudoku_solver import __version__
from sudoku_solver.sudoku import Sudoku


@pytest.fixture
def str_test_board():
    return "004006079000000602056092300078061030509000406020540890007410920105000000840600100"


""" Tests for sudoku_solver.sudoku """


def test_should_create_sudoku():
    assert Sudoku() is not None


def test_should_create_board_from_list_of_ints_0_to_9(str_test_board):
    test_board = [int(i) for i in str_test_board]

    sudoku = Sudoku()
    sudoku.load(test_board)

    assert sudoku.board is not None and len(sudoku.board) == 81


def test_valueerror_when_board_not_type_list(str_test_board):
    sudoku = Sudoku()
    # when not board not type list
    test_board = {i for i in str_test_board}

    with pytest.raises(ValueError):
        sudoku.load(test_board)
