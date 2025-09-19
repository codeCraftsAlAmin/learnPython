# # mapping in traditional way.
num = [1,2,3,4,5]

def myFunc(n):
    return n * n

res = list(map(myFunc, num))
print(res)

# # mapping in alternative way.
num2 = [1,2,3,4,5]

res = list([n + n for n in num2])
print(res)




# # filtering in traditional way.
num = [1,2,3,4,5]

def myFunc(n):
    return n > 3

res = list(filter(myFunc, num))
print(res)

# # filtering in alternatve way.
num2 = [1,2,3,4,5]

res = list([n for n in num2 if n > 4])
print(res)