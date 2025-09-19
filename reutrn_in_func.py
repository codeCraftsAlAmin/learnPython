# # return in function.

def add(a,b):
    sum =  a + b
    return sum

res = add(2,2)
print(res)

# # print largest number.

def largestNumb(a,b):
    if a > b:
        return a
    else:
        return b
    
res = largestNumb(3,6)
print(res)