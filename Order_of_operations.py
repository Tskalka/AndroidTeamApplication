from cgitb import text


def isFloat(text):
    try:   
         float(text)
         return True
    except:
        return False

def orderOfOperations(text):
    equation = []
    
    for item in text.split(' '):
        if isFloat(item):
            equation.append(item)

    for item in text.split(' '):
            if item == '+' or item == '-':
                num1 = int(equation[0])
                del equation[0]
                num2 = int(equation[0])
                del equation[0]
                if item == '+':
                    sum = num1 + num2
                    equation = [sum] + equation
                    print(sum)
                elif item == '-':
                    sum = num1 - num2
                    equation = [sum] + equation                    
                    print(sum)
    
    if len(equation) != 1:
        print("Error, Invalid input")

    print(equation)

orderOfOperations('10 + 2 + 3 - 6')