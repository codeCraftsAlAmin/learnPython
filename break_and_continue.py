# # Break: Terminate the current loop. Use the break statement to come out of the loop instantly.
numbers = [10, 20, 100, 140, 300]

for i in numbers:
    if i >= 100:
        break
    print("The number is",i)


# # continue: Skip the current iteration of a loop and move to the next iteration.
numbers = [2, 3, 11, 7]

for i in numbers:
    print("current number is", i)

    if i >= 10:
        continue

    square = i * i
    print("Square of a current number is", square)