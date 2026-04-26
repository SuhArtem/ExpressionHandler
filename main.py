

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
