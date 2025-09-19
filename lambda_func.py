# # Lambda function is an anonymous function, works with single line of code.

def clue(a,b):
    return a*a + 2*a*b + b*b
res = clue(2,3)
print(res)

# lambda = parameter : expression
n = (lambda a,b : a*a + 2*a*b + b*b)(2,3)
print(n)