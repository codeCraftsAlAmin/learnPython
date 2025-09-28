# # We can handle value error like this.

a = ["10", "twenty", 30]

try:
    res = int(a[0]) + int(a[5])
    print(res)
except (ValueError, TypeError, IndexError) as e:
    print(e)

finally:
    print("Process completed")


# # When you have to handle exception at function. 

def vote(age):
    if age < 18:
        raise ValueError("Voter isn't allowed")
    return print("You are allowed to vote")

try:
    vote(19)
except ValueError as e:
    print(e)


# # You can also create custom exceptions.

class AgeError(Exception):
    pass

def adult(age):
    if age < 18:
        raise AgeError("User isn't adult")
    return print("User is an adult")

try:
    adult(1)
except AgeError as e:
    print(e)
