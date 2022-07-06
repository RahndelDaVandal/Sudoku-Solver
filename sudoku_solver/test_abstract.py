from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Interface(ABC):
    value: int

    @staticmethod
    def try_inherit(v) -> None:
        print("Was Inherited", v)

    @abstractmethod
    def do_something(self) -> None:
        ...


class ConcreteA(Interface):
    def do_something(self) -> None:
        self.try_inherit(self.value)
        print("Doing Something")


concrete_a = ConcreteA(10)

print(concrete_a.value)

concrete_a.do_something()
