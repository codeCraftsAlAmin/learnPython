# # SET: order and duplicate value aren't allowed in set

num1 = {1,2,3,4,5}
num2 = set([5,6,7,8])

print(num1 | num2) # U
print(num1 & num2) # inter \ common number
print(num1 - num2) # diffe