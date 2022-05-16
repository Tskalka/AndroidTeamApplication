from cgitb import text

# Checks if the string input is a number
def isFloat(text):
    try:   
         float(text)
         return True
    except:
        return False


def orderOfOperations(text):
    equation = []

    #pulls only the number into the equation list
    for item in text.split(' '):
        if isFloat(item):
            equation.append(item)

    #checks for operators, does addition or subtraction 
    for item in text.split(' '):
            if item == '+' or item == '-':
                num1 = float(equation[0])
                del equation[0]
                num2 = float(equation[0])
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