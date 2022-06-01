plus = lambda a,b : a + b

ops1 = {'+' : plus }

ops2 = {'+' : (lambda a,b : a + b) }

print(ops1['+'](5,7))
print(ops2['+'](5,7))