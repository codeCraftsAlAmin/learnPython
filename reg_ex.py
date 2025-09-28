'''
# What is regEx?
- RegEx are tools to manipulating string.

# Why is regEx?
- Verify that strings match a pattern
- Permorming substituion in a string

# Use of regEx?
- regEx can be accessed by using the "re" module
- match(): matches at the begenning of a string
- search(): finds a match of a pattern anywhere in the string
- findall(): returns a list of all substrings that match a pattern
'''

# # match(): matches at the begenning of a string

import re

s = "Color is not colorfull"
p = r"Color"

if re.match(p, s):
    print("Pattern matched")
else:
    print("Pattern didn't matched")


# # search(): finds a match of a pattern anywhere in the string

import re

s = "Life is not full Color"
p = r"Color"

if re.search(p, s):
    print("Pattern matched")
else:
    print("Pattern didn't matched")


# # findall(): returns a list of all substrings that match a pattern

import re

s = "Life is not full Col,Color"
p = r"Col"

print(re.findall(p,s))


# # more

import re

s = "Life is not a bed of rose"

p = r"bed"

match = re.search(p,s)

if match:
    print(match.start())
    print(match.end())
else: 
    print("Didn't match")




'''
- sub(): find and replace
sub(pattern, replace, string)
'''

import re

s = "My favorite color is black, But I love blue color also"
p = r"color"

print(re.sub(p, "Colour", s, count=2)) # count=2 means it will replace 2 color words