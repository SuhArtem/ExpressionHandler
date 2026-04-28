from .BinaryOperation import *

class Exponential(BinaryOperation, ABC):

    def _priority(self):
        return Precedence.EXPONENTIAL.value


class Power(Exponential):

    def _sign(self) -> str:
        return "^"

    def evaluate(self, context=None):
        return self.arg1.evaluate(context) ** self.arg2.evaluate(context)