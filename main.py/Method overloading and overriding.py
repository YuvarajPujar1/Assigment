# Overloading 
class Calculator:
    # Method with default arguments to simulate overloading
    def add(self, a, b=0, c=0):
        return a + b + c

# Creating object of Calculator class
calc = Calculator()

# Calling method with different number of arguments
print(calc.add(5))         
print(calc.add(5, 10))    
print(calc.add(5, 10, 15)) 


#OverRidding 
class Animal:
    def make_sound(self):
        print("Animal makes a sound")

# Child class (Overriding the make_sound method)
class Dog(Animal):
    def make_sound(self):
        print("Dog barks")

# Creating objects
animal = Animal()
dog = Dog()

# Calling the method
animal.make_sound()  # Calls parent class method → Output: Animal makes a sound
dog.make_sound()     # Calls child class method → Output: Dog barks
