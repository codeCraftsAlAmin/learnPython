'''
In Python programming language there are two types of loops which are for loop and while loop. Using these loops we can create nested loops in Python. Nested loops mean loops inside a loop. For example, while loop inside the for loop, for loop inside the for loop, etc.
'''

'''
Python Nested Loops Syntax:

Outer_loop Expression:
    Inner_loop Expression:

        Statement inside inner_loop

    Statement inside Outer_loop
'''

x = [1,2,3]
y = [4,5,6]

for i in x:
    for j in y:
        print(i,j)


x = [1, 2]
y = [4, 5]

i = 0

while i < len(x):
    j = 0
    while j < len(y):
        print(x[i], y[j])

        j = j + 1
    i = i + 1

# # Printing multiplication table using Python nested for loops

for i in range(2,4):
    for j in range(1,11):
        print(i, "*", j, "=", i * j)
    print()


# # Example 3: Printing using different inner and outer nested loops

list1 = ['I am ', 'You are ']
list2 = ['healthy', 'fine', 'geek']

for item in list1:
    i = 0
    while i < len(list2):
        print(item, list2[i])
        i = i + 1
print("End of the loop")

# # Example 4: Use break in loop
for i in range(2,4):
    for j in range(1,11):
        if i == j:
            break
        print(i,"*",j, "=", i*j)
    print()