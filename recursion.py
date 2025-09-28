# # Recursion is a process where a function can call itself.
# # To stop this function we need a base case.

'''
best expample for recursion is factorial number like
4! = 4*3*2*1
3! = 3*2*1
2! = 2 * 1


or we can say that the factorial of 4! = 4*3!, 3! = 3*2!
so we can say n! = n*(n-1)!

'''

def fact(n):

    if n == 1:
        return 1 # base case to stop the function
    
    else:
        return n*fact(n-1)
    
print("factorial number is: ",fact(4))