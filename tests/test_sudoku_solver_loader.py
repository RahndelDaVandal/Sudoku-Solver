# test_sudoku_solver_loader.py

from sudoku_solver import __version__
from sudoku_solver.loader import Loader
from sudoku_solver.loader.strategy import FromSRM, FromTXT


""" Tests for sudoku_solver.loader Loader """


def test_should_create_Loader():
    loader = Loader()
    assert loader is not None


def test_defaut_Loader_strategy_should_be_FromSRM():
    loader = Loader()
    assert type(loader.strategy) == FromSRM


def test_set_Loader_strategy_to_FromTXT_after_creation():
    loader = Loader()
    loader.strategy = FromTXT()
    assert type(loader.strategy) == FromTXT


""" Tests for sudoku_solver.loader.strategy """


def test_should_create_strategy_FromSRM():
    strategy = FromSRM()
    assert strategy is not None
