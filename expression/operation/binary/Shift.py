from .BinaryOperation import *

class Shift(BinaryOperation, ABC):

    def _priority(self):
        return Precedence.SHIFT.value

class LSL(Shift):

    def _sign(self):
        return "<<"

    def evaluate(self, context=None):
        return self.arg1.evaluate(context) << self.arg2.evaluate(context)

class ASR(Shift):

    def _sign(self):
        return ">>"

    def evaluate(self, context=None):
        return self.arg1.evaluate(context) >> self.arg2.evaluate(context)