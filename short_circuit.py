# # short circuit.
marks = 70

if marks >= 80 and marks <= 100:
    print("A+")
elif marks >= 70 and marks <= 79:
    print("A")
elif marks >= 60 and marks <= 69:
    print("A-")
else: 
    print("None of these")

# #  ---------or---------
if 80 <= marks <= 100:
    print("A+")
elif 70 <= marks <= 79:
    print("A")
elif 60 <= marks <= 69:
    print("A-")
else: print("None of these")