# test_sudoku_solver_solver.py

from sudoku_solver import __version__
from sudoku_solver.solver import Solver
from sudoku_solver.solver.strategy import (
        BackTrack,
        BackTrackRandomStart,
        BackTrackRandomIndex,
        Possibilities
        )


def test_version():
    assert __version__ == '0.1.0'


""" Tests for sudoku_solver.solver Solver"""


def test_should_create_Solver():
    assert Solver() is not None


def test_solver_defaults_to_BackTrack():
    assert type(Solver().strategy) == BackTrack


def test_set_strategy_to_possibilities_Solver_creation():
    s = Solver(Possibilities())
    assert type(s.strategy) == Possibilities


def test_set_to_different_strategies_after_Solver_creation():
    strategies = {
            BackTrack: BackTrack(),
            BackTrackRandomStart: BackTrackRandomStart(),
            BackTrackRandomIndex: BackTrackRandomIndex(),
            Possibilities: Possibilities()
            }

    solver = Solver()

    for k, v in strategies.items():
        solver.strategy = v
        assert type(solver.strategy) == k


""" Tests for sudoku_solver.solver startegy """


def test_should_create_BackTrack_Strategy():
    strat = BackTrack()
    assert type(strat) == BackTrack


def test_should_create_BackTrackRandomStart_Strategy():
    strat = BackTrackRandomStart()
    assert type(strat) == BackTrackRandomStart


def test_should_create_BackTrackRandomIndex_Strategy():
    strat = BackTrackRandomIndex()
    assert type(strat) == BackTrackRandomIndex


def test_should_create_Possibilities_Strategy():
    strat = Possibilities()
    assert type(strat) == Possibilities




