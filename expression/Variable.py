from .Expression import Expression
from typing import Mapping

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
            raise TypeError(f"'==' not supported between instances of '{self.__class__.__name__}' " +
                            f"and '{other.__class__.__name__}'")
        return isinstance(other, Variable) and self._name == other._name

    def evaluate(self, context):
        if isinstance(context, Mapping):
            return context[self._name]
        elif isinstance(context, list):
            return context[self._index]
        return context
