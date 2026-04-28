from expression.Expression import Expression


class Functional(Expression): # TODO: Other functional classes should be implemented.

    def __init__(self, args: list[Expression], name: str):
        self._args: list[Expression] = args
        self._name: str = name


    def __eq__(self, other):
        return isinstance(other, Functional) and other._args == self._args


    def evaluate(self, context=None):
        toInt = []
        for i in self._args:
            toInt.append(i.evaluate(context))
        return func_name[self._name](toInt)

    def __str__(self):
        return f"{self._name}({','.join(str(i) for i in self._args)})"

    def toMiniString(self):
        ExpToStr = []
        for i in self._args:
            ExpToStr.append(i.toMiniString())
        return f"{self._name}({','.join(ExpToStr)})"


func_name = {
    'min': min
}
