from enum import Enum, auto


class LexemeType(Enum):
    LEFT_BRACKET = auto()
    RIGHT_BRACKET = auto()
    COMMA = auto()
    FUNC_NAME = auto()
    OP_LT = auto()
    OP_GT = auto()
    OP_LE = auto()
    OP_GE = auto()
    OP_EQ = auto()
    OP_NEQ = auto()
    OP_PLUS = auto()
    OP_MINUS = auto()
    OP_LSL = auto()
    OP_ASR = auto()
    OP_MUL = auto()
    OP_DIV = auto()
    OP_EXP = auto()
    NUMBER = auto()
    VARIABLE = auto()
    EOF = auto()


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
        self.string: str = string

        # self.BigNameOperation = {
        #     "<<": "LSL"
        # }

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
                case ",":
                    lexemes.append(Lexeme(LexemeType.COMMA, self.string[i]))
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
                case "^":
                    lexemes.append(Lexeme(LexemeType.OP_EXP, self.string[i]))
                    i += 1
                    continue
                case "$":
                    lexemes.append(Lexeme(LexemeType.VARIABLE, self.string[i]))
                    i += 1
                    continue
            if '0' <= self.string[i] <= '9':
                number = []
                while i < len(self.string) and '0' <= self.string[i] <= '9':
                    number.append(self.string[i])
                    i += 1
                lexemes.append((Lexeme(LexemeType.NUMBER, ''.join(number))))
                i -= 1
            elif self.string[i] in "<>=!":
                operation = []
                while i < len(self.string) and self.string[i] in "<>=!":
                    operation.append(self.string[i])
                    i += 1
                op = ''.join(operation)
                match op:
                    case "<<":
                        lexemes.append(Lexeme(LexemeType.OP_LSL, op))
                        continue
                    case ">>":
                        lexemes.append(Lexeme(LexemeType.OP_ASR, op))
                        continue
                    case "<":
                        lexemes.append(Lexeme(LexemeType.OP_LT, op))
                        continue
                    case ">":
                        lexemes.append(Lexeme(LexemeType.OP_GT, op))
                        continue
                    case "<=":
                        lexemes.append(Lexeme(LexemeType.OP_LE, op))
                        continue
                    case ">=":
                        lexemes.append(Lexeme(LexemeType.OP_GE, op))
                        continue
                    case "==":
                        lexemes.append(Lexeme(LexemeType.OP_EQ, op))
                        continue
                    case "!=":
                        lexemes.append(Lexeme(LexemeType.OP_NEQ, op))
                        continue
                    case _:
                        raise SyntaxError(f'Unexpected token at {op}') # --
            elif self.string[i].isalpha():
                funcName = []
                while i < len(self.string) and self.string[i].isalpha():
                    funcName.append(self.string[i])
                    i += 1
                lexemes.append(Lexeme(LexemeType.FUNC_NAME, ''.join(funcName)))
                i -= 1
            else:
                if self.string[i] != ' ':
                    raise SyntaxError('Incorrect expression input')
            i += 1
        lexemes.append(Lexeme(LexemeType.EOF, ''))
        return lexemes