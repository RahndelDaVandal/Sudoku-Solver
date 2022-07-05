# sudoku_solver.loader.stategy.py
from abc import ABC, abstractmethod


class Strategy(ABC):

    @abstractmethod
    def load(self, file_path: str) -> list[int]:
        pass


class FromSRM(Strategy):

    def load(self, file_path: str) -> list[int]:
        print("FromSRM Loader Strategy Executed")
