from expression.operation.binary.BinaryOperation import ABC, BinaryOperation, Precedence

class Additive(BinaryOperation, ABC):

    def _priority(self):
        return Precedence.ADDITIVE.value


class Add(Additive):

    def _sign(self) -> str:
        return "+"

    def evaluate(self, context=None):
        return self.arg1.evaluate(context) + self.arg2.evaluate(context)

class Subtract(Additive):

    def _sign(self) -> str:
        return "-"

    def evaluate(self, context=None):
        return self.arg1.evaluate(context) - self.arg2.evaluate(context)