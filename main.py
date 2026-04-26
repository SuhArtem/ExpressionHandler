"""
ExpressionHandler is a class that processes the expression that looks like a string

ExpressionHandler(expression: str).expr() returns an object of BinaryOperation class type
or int if expression which the passed to the class is empty string

BinaryOperation class inherit from Expression Abstract Base Class

-------
An object of class BinaryOperation has a method evaluate that evaluates the expression
If expression contains a different variables
then parameters of method should be list[int] or dict['${number of variable}': value]

The values of the variables will be taken from
the list by index corresponding to the variable number or from
the dict by name corresponding to the variable name
-------

correct entry of an expression with variables
1. a$0*$0 + b*$0 + c -> a*x^2 + b*x + c
2. $0*$0 + $1*$1 + const -> x^2 + y^2 + const
3. $0*2       -13/(2   +4    )*$2

For example:
expression = "0 + ($0 + $1) * $2*$2 - 12 / 4"
expr = ExpressionHandler(expression).expr()
print(expr) # -> ((0 + ((($0 + $1) * $2) * $2)) - (12 / 4))
print(expr.toMiniString()) # -> ((0 + ((($0 + $1) * $2) * $2)) - (12 / 4))
print(expr.evaluate([1, 2, 3])) # -> 24
print(expr.evaluate({
    '$0': 2,
    '$1': 3,
    "$2": 4
})) # -> 77

If you want to evaluate an expression from the console,
you need to enclose the mathematical expression in quotes
and then specify the variables as a dictionary: `$i=val`
if the variables exist in the expression.
For example: python3 main.py '$0*$1 + 1 - 12 / 4' '$0=10' '$1=17'
Then you will get the result of the calculation -> result: 168

"""

from ExpressionHandler import ExpressionHandler
import sys

def toDict(array):
    d = {}
    for i in array:
        key, val = i.split("=")
        if key not in d:
            d[key] = int(val)
    return d

def main():

    baseExpression = "$0*$0 + 2*$0 + 1"
    baseVar = {
        "$0": 1
    }

    args = sys.argv[1:]
    if not args:
        print("You start the program without parameters")
        print(f"You will get the base expression: {baseExpression} with arguments: " +
              f"{[f"{k}={v}" for k, v in baseVar.items()]}")
        print("The result: ", str(ExpressionHandler(baseExpression).expr().evaluate(baseVar)))
    else:
        expression = args[0]
        variable = toDict(args[1:])
        print(ExpressionHandler(expression).expr().evaluate(variable))


if __name__ == "__main__":
    main()
