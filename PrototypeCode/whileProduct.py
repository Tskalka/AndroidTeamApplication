equation = []

text = "5 + 3 * 2 - 4 * 6"
for item in text.split(' '):
    equation.append(item)

print(equation)
myIndex = equation.index('*')
result = int(equation[myIndex - 1]) * int(equation[myIndex + 1])
print(result)
del equation[myIndex - 1]
del equation[myIndex - 1]
equation[myIndex - 1] = result

print(equation)
myIndex = equation.index('*')

result = int(equation[myIndex - 1]) * int(equation[myIndex + 1])
print(result)
del equation[myIndex - 1]
del equation[myIndex - 1]
equation[myIndex - 1] = result

print(equation)