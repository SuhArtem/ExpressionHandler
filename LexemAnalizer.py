from Expression import Expression
from enum import Enum


class LexemeType(Enum):
    LEFT_BRACKET = 1
    RIGHT_BRACKET = 2
    OP_PLUS = 3
    OP_MINUS = 4
    OP_MUL = 5
    OP_DIV = 6
    NUMBER = 7
    VARIABLE = 8
    EOF = 9


class Lexeme:
    type: LexemeType
    value: str

    def __init__(self, type: LexemeType, value: str):
        self.type = type
        self.value = value


class LexemeBuffer:

    def __init__(self, lexemes: list[Lexeme]):
        self.pos = 0
        self.lexemes = lexemes

    def next(self):
        el = self.lexemes[self.pos]
        self.pos += 1
        return el

    def back(self):
        self.pos -= 1

    def getPos(self):
        return self.pos


class LexemeAnalyzer:

    def __init__(self, string):
        self.string = string

    def lexemeAnalyzer(self) -> list[Lexeme]:
        lexemes = []
        i = 0
        while i < len(self.string):
            match self.string[i]:
                case "(":
                    lexemes.append(Lexeme(LexemeType.LEFT_BRACKET, self.string[i]))
                    i += 1
                    continue
                case ")":
                    lexemes.append(Lexeme(LexemeType.RIGHT_BRACKET, self.string[i]))
                    i += 1
                    continue
                case "+":
                    lexemes.append(Lexeme(LexemeType.OP_PLUS, self.string[i]))
                    i += 1
                    continue
                case "-":
                    lexemes.append(Lexeme(LexemeType.OP_MINUS, self.string[i]))
                    i += 1
                    continue
                case "*":
                    lexemes.append(Lexeme(LexemeType.OP_MUL, self.string[i]))
                    i += 1
                    continue
                case "/":
                    lexemes.append(Lexeme(LexemeType.OP_DIV, self.string[i]))
                    i += 1
                    continue
                case "$":
                    lexemes.append(Lexeme(LexemeType.VARIABLE, self.string[i]))
                    i += 1
                    continue
            if '0' <= self.string[i] <= '9':
                st = ''
                k = i
                while k < len(self.string) and '0' <= self.string[k] <= '9':
                    st += self.string[k]
                    k += 1

                lexemes.append((Lexeme(LexemeType.NUMBER, st)))
                i = k - 1
            else:
                if self.string[i] != ' ':
                    raise SyntaxError('Incorrect expression input')
            i += 1
        lexemes.append(Lexeme(LexemeType.EOF, ''))
        return lexemes