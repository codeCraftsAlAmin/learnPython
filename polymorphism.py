# # Compile-time Polymorphism.

class MathOps:
    
    def add(self,a,b,*numbers):
        res = a + b

        for num in numbers:
            res += num
        return res
    
m = MathOps()
print(m.add(2,3))
print(m.add(2,3,4))
print(m.add(1,2,3,4))


# # Runtime Polymorphism (Overriding).

class Animal:
    def sound(self):
        return "Some generic sound"
    

class Dog(Animal):
    def sound(self):
        return "Bark"
    
class Cat(Animal):
    def sound(self):
        return "Meow"
    
# Polymorphic behavior

animals = [Cat(), Dog(), Animal()]

for animal in animals:
    print(animal.sound())


# # Polymorphism in Functions.

class Pen:
    def use(self):
        return "Writing"
    
class Eraser:
    def use(self):
        return "Erasing"

def perform_task(tool):
    print(tool.use())


perform_task(Pen())
perform_task(Eraser())


class Calculate:

    def multiply(self, a,b,*args):
        result = a * b

        for arg in args:
            result *= arg
        return result
    
calc = Calculate()
print(calc.multiply(5,2))
