# # To read a txt file

'''
file name = "student.txt"
state(reading, writing or both)= "r" / "w" / "r+"
'''

file = open("students.txt", "r")


# print(file.readable()) # # to check if the file is readable
# print(file.writable()) # # to check if the file is writeable


text = file.read() # to read file
# text = file.readlines() # # to read as a list
print(text)

file.close() # close file