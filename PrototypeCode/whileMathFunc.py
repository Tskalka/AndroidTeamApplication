import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor,
}

def doMath(oper, equation):
    myIndex = equation.index(oper)
    result = ops[oper](int(equation[myIndex - 1]), int(equation[myIndex + 1]))
    print(result)
    del equation[myIndex - 1]
    del equation[myIndex - 1]
    equation[myIndex - 1] = result
    print(equation)


equation = []
operators = ['*','/','+','-']
text = "5 + 3 * 2 - 4 * 6"
for item in text.split(' '):
    equation.append(item)

for oper in operators:
    while oper in equation:
        doMath(oper, equation)