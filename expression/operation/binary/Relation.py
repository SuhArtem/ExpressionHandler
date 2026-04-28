
__all__ = ['Gt', 'Lt', 'Ge', "Le", 'Eq', 'Neq']

from .BinaryOperation import *

class Relation(BinaryOperation, ABC):

    def _priority(self):
        return Precedence.RELATION.value

class Gt(Relation):

    def _sign(self):
        return ">"
    def evaluate(self, context=None):
        return int(self.arg1.evaluate(context) > self.arg2.evaluate(context))

class Lt(Relation):

    def _sign(self):
        return "<"

    def evaluate(self, context=None):
        return int(self.arg1.evaluate(context) < self.arg2.evaluate(context))

class Le(Relation):

    def _sign(self):
        return "<="

    def evaluate(self, context=None):
        return int(self.arg1.evaluate(context) <= self.arg2.evaluate(context))

class Ge(Relation):

    def _sign(self):
        return ">="

    def evaluate(self, context=None):
        return int(self.arg1.evaluate(context) >= self.arg2.evaluate(context))

class Eq(Relation):

    def _sign(self):
        return "=="

    def evaluate(self, context=None):
        return int(self.arg1.evaluate(context) == self.arg2.evaluate(context))

class Neq(Relation):

    def _sign(self):
        return "!="

    def evaluate(self, context=None):
        return int(self.arg1.evaluate(context) != self.arg2.evaluate(context))