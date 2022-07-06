# test_board.py
import pytest

from sudoku_solver import __version__
from sudoku_solver.board import Board


@pytest.fixture
def str_test_board():
    s = "00400607900000060205609230007806103050900"
    s += "0406020540890007410920105000000840600100"
    return s


@pytest.fixture
def test_board(str_test_board):
    return [i for i in str_test_board]


@pytest.fixture
def test_blanks(test_board):
    return [i for i, v in enumerate(test_board) if v == 0]


def test_version():
    assert __version__ == '0.1.0'


def test_should_create_Board():
    assert Board() is not None


def test_should_set_board(test_board):
    assert Board(test_board).board == test_board


def test_setting_board_should_set_blanks(test_board, test_blanks):
    board = Board()
    board.board = test_board
    assert board._blanks == test_blanks
