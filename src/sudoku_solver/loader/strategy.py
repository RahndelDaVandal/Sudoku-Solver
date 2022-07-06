# sudoku_solver.loader.stategy.py
from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class Strategy(ABC):
    _target: str = None

    @property
    def target(self) -> str:
        return self._target

    @target.setter
    def target(self, target: str) -> None:
        if not isinstance(target, str):
            raise ValueError("target must be type string")
        self._target = target

    @abstractmethod
    def load(self, file_path: str) -> list[int]:
        pass


class FromSTR(Strategy):
    def load(self) -> list[int]:
        print("FromSTR Loader Strategy Executed")


class FromSRM(Strategy):
    def load(self, file_path: str) -> list[int]:
        print("FromSRM Loader Strategy Executed")


class FromTXT(Strategy):
    def load(self, file_path: str) -> list[int]:
        print("FromTXT Loader Strategy Executed")
