# get list as input from user

num = "10 20 30"

list = num.split() # convert numbers into list

sum = 0

for x in list:
    sum = sum + int(x) # convert numberes into int

print(sum)


# # count letter word and digit from a text.

numberOfWords = 0
numberOfDigits = 0
numberOfSLetters = 0

text = "the initial number is 01"

for x in text:

    x = x.lower()

    if x >= 'a' and x <= 'z':
        numberOfSLetters = numberOfSLetters + 1
    elif x >= '0' and x <= '9':
        numberOfDigits = numberOfDigits + 1
    elif x == ' ':
        numberOfWords = numberOfWords + 1

print("number of words: ",numberOfWords + 1)
print("number of letters: ",numberOfSLetters)
print("number of digits: ",numberOfDigits)