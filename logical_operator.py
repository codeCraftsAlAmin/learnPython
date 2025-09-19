# # logical operator AND.

num1 = 10
num2 = 30
num3 = 20

if num1 > num2 and  num1 > num3:
    print(num1)
elif num2 > num1 and  num2 > num3:
    print(num2)
else:
    print(num3)


# # logical operator OR.

letter = "e"

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("Vowel")
else:
    print("Consonant")
