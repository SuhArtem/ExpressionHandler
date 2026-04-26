
from abc import ABC, abstractmethod
from typing import Mapping


class Expression(ABC):

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def evaluate(self, context):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def toMiniString(self):
        pass


class Const(Expression):

    def __init__(self, val):
        if not isinstance(val, int):
            raise TypeError("Only integer may be Const")
        self._val = val

    @property
    def val(self):
        return self._val

    def __str__(self):
        return str(self._val)

    def toMiniString(self):
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, Expression):
            raise TypeError(f"Comparison type error {self.__class__.__name__}" +
                            f" and {other.__class__.__name__}")
        return isinstance(other, Const) and self._val == other._val

    def evaluate(self, context=None):
        return self._val

class Variable(Expression):

    def __init__(self, index: int):
        self._index = index
        self._name = f"${index}"

    def __str__(self):
        return self._name

    def toMiniString(self):
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, Expression):
            raise TypeError(f"Comparison type error {self.__class__.__name__} and {other.__class__.__name__}")
        return isinstance(other, Variable) and self._name == other._name

    def evaluate(self, context):
        if isinstance(context, Mapping):
            return context[self._name]
        elif isinstance(context, list):
            return context[self._index]
        return context

