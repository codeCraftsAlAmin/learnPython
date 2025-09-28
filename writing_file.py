# # To writing in a file.

'''
- 'a' means append, means adding a new line with existing code.
- 'w' it will overwrite the previous code
'''

file = open("students.txt", "a")  
# print(file.writable())

file.write("\nSadi - Physics lecturer")

file.close()