# # A Class: in Python is a user-defined template for creating objects.
# # An object: is a specific instance of a class.


'''
Why do we need Classes and Objects
- Supports object-oriented programming using reusable templates (classes) and real-world models (objects).
- Promotes code reusability and modular design with organized methods and attributes.
- Simplifies complex programs by grouping related data and behavior.
- Enables key OOP concepts like inheritance, encapsulation and polymorphism.
'''

# # Ex-1.
class Dog:
    sound = "bark"
    color = "white"
    gender = "male"


dog1 = Dog() # object
dog2 = Dog() # object
dog3 = Dog() # object
print(dog1.sound)
print(dog2.color)
print(dog1.gender)

# # Ex-2.
class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)

print(dog1.name)  
print(dog1.species)

# # Ex-3.
class Students:
    # Class variable
    section = "A"

    def __init__(self, name, roll, gpa):
        # Instance variables
        self.name = name
        self.roll = roll
        self.gpa = gpa

    def __str__(self):
        return f"name: {self.name}, roll: {self.roll}, gpa: {self.gpa}"
    
s1 = Students("Abir", 23, 4.55)
s2 = Students("Tanvir", 13, 4.00)
s3 = Students("Rifat", 2, 5.00)

print(f"Result of section: {s1.section}")

print(s1)
print(s2)
print(s3)


# # Ex.

class Triangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height


    def calculate_area(self):
        area = 1/2*self.base*self.height
        print(f"Area = {area}")

t1 = Triangle(10, 20)
t1.calculate_area()

t2 = Triangle(20, 30)
t2.calculate_area()