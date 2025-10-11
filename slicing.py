'''
String slicing in Python is a way to get specific parts of a string by using start, end and step values. It’s especially useful for text manipulation and data parsing.
'''
'''
substring = s[start : end : step]
'''

t = "Al Amin Ahmed"
print(t[0:5])


'''
Negative indexing is useful for accessing elements from the end of the String. The last element has an index of -1, the second last element -2 and so on.
'''


s = "abcdefgh"
print(s[-3:])
print(s[:-4])
print(s[-3:-1])
print(s[0:-2:2])


'''
To reverse a string, use a negative step value of -1, which moves from the end of the string to the beginning.
'''
p = "Python"
print(p[::-1])