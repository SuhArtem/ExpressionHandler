from expression.Expression import Expression
from abc import ABC, abstractmethod
from enum import Enum, auto

class Precedence(Enum):
    """This enumeration class specifies the priority of binary operations from low to high."""

    LOGICAL = auto()
    ADDITIVE = auto()
    SHIFT = auto()
    MULTIPLICATIVE = auto()
    EXPONENTIAL = auto()
    RELATION = auto()


class BinaryOperation(Expression, ABC):

    def __init__(self, arg1: Expression, arg2: Expression) -> None:
        self.arg1 = arg1
        self.arg2 = arg2

    @abstractmethod
    def _sign(self) -> str:
        ...

    @abstractmethod
    def _priority(self) -> int:
        ...

    def __str__(self):
        return f"({self.arg1} {self._sign()} {self.arg2})"

    def toMiniString(self):
        arg1Str = self.strHandler(self.arg1)
        arg2Str = self.strHandler(self.arg2)

        return f"{arg1Str} {self._sign()} {arg2Str}"

    def __eq__(self, other):
        if not isinstance(other, Expression):
            raise TypeError(
                f"You cannot compare an object of {self.__class__.__name__} " +
                f"with an object of {self.__class__.__name__}")
        return isinstance(other, self.__class__) and self.arg1 == other.arg1 and self.arg2 == other.arg2

    def strHandler(self, arg: Expression):
        if isinstance(arg, BinaryOperation) and self._priority() > arg._priority():
            return f"({arg.toMiniString()})"
        return arg.toMiniString()

