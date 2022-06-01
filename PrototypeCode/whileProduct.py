#We are creating a list where the equation is going to be located. 
equation = [] 

text = "5 + 3 * 2 - 4 * 6" #Equation we want to work on with the "Text variable"
#We are spliting the equation in its own index and then append them into the equation list
for item in text.split(' '):
    equation.append(item)

#printing equation to show the procces
print(equation) 

#This is the when we are taking the multiplication index and we are doing the math
#the result variable is taking the past and future index where the multiplication is to perform the math
#we are deleting the indexes used in the list and the result of it 
myIndex = equation.index('*')
result = int(equation[myIndex - 1]) * int(equation[myIndex + 1])
print(result)
del equation[myIndex - 1]
del equation[myIndex - 1]
equation[myIndex - 1] = result

#Print the equation again. (we might have to use a while statement in the future). 
print(equation)

#Proccess start again: 
myIndex = equation.index('*')

result = int(equation[myIndex - 1]) * int(equation[myIndex + 1])
print(result)
del equation[myIndex - 1]
del equation[myIndex - 1]
equation[myIndex - 1] = result

print(equation)