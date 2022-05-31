import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.pow,
}

def doMath(oper, equation):
    myIndex = equation.index(oper)
    result = ops[oper](int(equation[myIndex - 1]), int(equation[myIndex + 1]))
    print(result)
    del equation[myIndex - 1]
    del equation[myIndex - 1]
    equation[myIndex - 1] = result
    print(equation)
    return equation

def runEquation(equation):
    operators = ['^','*','/','+','-']
    for oper in operators:
     while oper in equation:
        newEquation = doMath(oper, equation)
    #print(newEquation)
    return newEquation

equation = []

text = "( 5 + 3 ) + ( 2 - 5 * 3 ^ 2 )"
for item in text.split(' '):
    equation.append(item)

while len(equation) > 1:
    if '(' not in equation:
        print(runEquation(equation))
    else:
        myIndex = equation.index('(')
        subEquation = []
        count = 1
        while equation[myIndex + count] != ')':
            subEquation.append(equation[myIndex + count])
            count += 1
        innerMath = runEquation(subEquation)
        for i in range(count):
            del equation[myIndex]
        equation[myIndex] = innerMath[0]
        
