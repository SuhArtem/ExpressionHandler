from .BinaryOperation import *


class Multiplicative(BinaryOperation, ABC):

    def _priority(self):
        return Precedence.MULTIPLICATIVE.value


class Multiply(Multiplicative):

    def _sign(self) -> str:
        return "*"

    def evaluate(self, context=None):
        return self.arg1.evaluate(context) * self.arg2.evaluate(context)


class Divide(Multiplicative):

    def _sign(self) -> str:
        return "/"

    def evaluate(self, context=None):
        return self.arg1.evaluate(context) // self.arg2.evaluate(context)