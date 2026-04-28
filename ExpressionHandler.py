
from expression.operation import *
from expression.Const import Const
from expression.Variable import Variable
from handlers.LexemAnalizer import *
from expression.functional import Functional, func_list

class ExpressionHandler:

    def __init__(self, expression: str):
        self.lexemes = LexemeBuffer(LexemeAnalyzer(expression).lexemeAnalyzer())

    def expr(self):
        lexeme = self.lexemes.next()
        if lexeme.type == LexemeType.EOF:
            return -1
        else:
            self.lexemes.back()
            return self.relation()

    def relation(self):
        value = self.plusminus()
        while True:
            lexeme = self.lexemes.next()
            match lexeme.type:
                case LexemeType.OP_LT:
                    value = Lt(value, self.plusminus())
                case LexemeType.OP_GT:
                    value = Gt(value, self.plusminus())
                case LexemeType.OP_LE:
                    value = Le(value, self.plusminus())
                case LexemeType.OP_GE:
                    value = Ge(value, self.plusminus())
                case LexemeType.OP_EQ:
                    value = Eq(value, self.plusminus())
                case LexemeType.OP_NEQ:
                    value = Neq(value, self.plusminus())
                case _:
                    self.lexemes.back()
                    return value

    def plusminus(self):
        value = self.shift()
        while True:
            lexeme = self.lexemes.next()
            match lexeme.type:
                case LexemeType.OP_PLUS:
                    value = Add(value, self.shift())
                case LexemeType.OP_MINUS:
                    value = Subtract(value, self.shift())
                case _:
                    self.lexemes.back()
                    return value

    def shift(self):
        value = self.muldiv()
        while True:
            lexeme = self.lexemes.next()
            match lexeme.type:
                case LexemeType.OP_LSL:
                    value = LSL(value, self.muldiv())
                case LexemeType.OP_ASR:
                    value = ASR(value, self.muldiv())
                case _:
                    self.lexemes.back()
                    return value

    def muldiv(self):
        value = self.factor()
        while True:
            lexeme = self.lexemes.next()
            match lexeme.type:
                case LexemeType.OP_MUL:
                    value = Multiply(value, self.factor())
                case LexemeType.OP_DIV:
                    value = Divide(value, self.factor())
                case LexemeType.OP_EXP:
                    value = Power(value, self.factor())
                case _:
                    self.lexemes.back()
                    return value

    def factor(self):
        lexeme = self.lexemes.next()
        match lexeme.type:
            case LexemeType.FUNC_NAME:
                return self.func(lexeme)
            case LexemeType.VARIABLE:
                index = self.factor()
                return Variable(index.val)
            case LexemeType.OP_MINUS:
                value = self.factor()
                return Const(-value.val)
            case LexemeType.RIGHT_BRACKET:
                return
            case LexemeType.COMMA:
                return
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

    def func(self, name: Lexeme) -> Functional:
        name = name.value
        if name not in func_list:
            raise SyntaxError(f"Invalid function name: {name}")

        lexeme = self.lexemes.next()

        if lexeme.type != LexemeType.LEFT_BRACKET:
            raise SyntaxError(f"Invalid function syntaxis. Missing left parenthesis")

        args = []

        lexeme = self.lexemes.next()
        if lexeme.type != LexemeType.RIGHT_BRACKET:
            self.lexemes.back()
            args.append(self.expr())
            lexeme = self.lexemes.next()
            while lexeme.type == LexemeType.COMMA:
                args.append(self.expr())
                lexeme = self.lexemes.next()
        if lexeme.type != LexemeType.RIGHT_BRACKET:
            raise SyntaxError("Invalid function syntaxis. Missing Right parenthesis")
        return Functional(args, name)
