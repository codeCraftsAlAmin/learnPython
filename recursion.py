'''
Recursion is a programming technique where a function calls itself either directly or indirectly to solve a problem by breaking it into smaller, simpler subproblems.
'''

'''
Syntax: 
def recursive_function(parameters):
    if base_case_condition:
        return base_result
    else:
        return recursive_function(modified_parameters)
'''

def fact(n):

    if n == 1:
        return 1 # base case to stop the function
    
    else:
        return n*fact(n-1)
    
print("factorial number is: ",fact(4))


'''
The Fibonacci sequence is a series of numbers where:
each number = sum of the previous two numbers.
'''


def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(7))


'''
Types of Recursion in Python
Recursion can be broadly classified into two types: tail recursion and non-tail recursion. The main difference between them is related to what happens after recursive call.

Tail Recursion: The recursive call is the last thing the function does, so nothing happens after it returns. Some languages can optimize this to work like a loop, saving memory.
Non-Tail Recursion: The function does more work after the recursive call returns, so it can’t be optimized into a loop.
'''


def tail_fact(n, acc=1):
    if n == 0:
        return acc
    else:
        return tail_fact(n-1, acc*n)

print(tail_fact(3))

def nontail_fact(n):
    if n==1:
        return 1
    else:
        return n*nontail_fact(n-1)
print(nontail_fact(4))