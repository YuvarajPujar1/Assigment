# Class & Object
class Animal:
    def __init__(self, name):
        self.name = name  # Encapsulation: Storing data inside the class
    
    def make_sound(self):
        print(self.name, "makes a sound.")

# Inheritance: Dog class inherits from Animal
class Dog(Animal):
    def make_sound(self):  # Overriding method
        print(self.name, "barks!")

# Creating objects
animal = Animal("Some Animal")
dog = Dog("Buddy")

# Calling methods
animal.make_sound()
dog.make_sound()
