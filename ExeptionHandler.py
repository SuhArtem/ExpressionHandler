
from BinaryOperation import *
from Expression import *
from LexemAnalizer import *

class ExpressionHandler:

    def __init__(self, expression: str):
        self.lexemes = LexemeBuffer(LexemeAnalyzer(expression).lexemeAnalyzer())

    def expr(self):
        lexeme = self.lexemes.next()
        if lexeme.type == LexemeType.EOF:
            return 0
        else:
            self.lexemes.back()
            return self.plusminus()

    def plusminus(self):
        value = self.muldiv()
        while True:
            lexeme = self.lexemes.next()
            if lexeme.type == LexemeType.OP_PLUS:
                value = Add(value, self.muldiv())
            elif lexeme.type == LexemeType.OP_MINUS:
                value = Subtract(value, self.muldiv())
            else:
                self.lexemes.back()
                return value

    def muldiv(self):
        value = self.factor()
        while True:
            lexeme = self.lexemes.next()
            if lexeme.type == LexemeType.OP_MUL:
                value = Multiply(value, self.factor())
            elif lexeme.type == LexemeType.OP_DIV:
                value = Divide(value, self.factor())
            else:
                self.lexemes.back()
                return value

    def factor(self):
        lexeme = self.lexemes.next()
        match lexeme.type:
            case LexemeType.VARIABLE:
                index = self.factor()
                return Variable(index.val)
            case LexemeType.OP_MINUS:
                value = self.factor()
                return Const(-value.val)
            case LexemeType.NUMBER:
                return Const(int(lexeme.value))
            case LexemeType.LEFT_BRACKET:
                val = self.expr()
                lexeme = self.lexemes.next()
                if lexeme.type != LexemeType.RIGHT_BRACKET:
                    raise SyntaxError("Unexpected token " + str(lexeme.value) +
                                      " at position " + str(self.lexemes.getPos()))
                return val
        raise SyntaxError("Unexpected token " + str(lexeme.value) +
                          " at position " + str(self.lexemes.getPos()))
