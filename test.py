from ExpressionHandler import ExpressionHandler


baseExpression = "min(min($0, $1), $2)" # x^2 + 2*x + 1
baseVar = {
    "$0": 1 # x = 1
}
a = ExpressionHandler(baseExpression).expr()

print(a.evaluate([5, 2, 3]))