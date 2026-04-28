from .Expression import Expression

class Const(Expression):

    def __init__(self, val):
        if not isinstance(val, int):
            raise TypeError(f"Const should be contains only integer. But was given {val.__class__.__name__}")
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
            raise TypeError(f"'==' not supported between instances of '{self.__class__.__name__}' " +
                            f"and '{other.__class__.__name__}'")
        return isinstance(other, Const) and self._val == other._val

    def __lt__(self, other):
        return self._val < other._val

    def evaluate(self, context=None):
        return self._val