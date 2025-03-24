# Method Overloading (Using Default Arguments)
class MathOperations:
    def add(self, a, b=0, c=0):
        return a + b + c  # Handles 1, 2, or 3 parameters

# Method Overriding (Using Inheritance)
class Parent:
    def show(self):
        print("This is the Parent class method.")

class Child(Parent):
    def show(self):  # Overriding Parent's method
        print("This is the Child class method.")

# Testing Method Overloading
math_obj = MathOperations()
print("Sum with 1 argument:", math_obj.add(5))
print("Sum with 2 arguments:", math_obj.add(5, 10))
print("Sum with 3 arguments:", math_obj.add(5, 10, 15))

# Testing Method Overriding
obj1 = Parent()
obj2 = Child()

obj1.show()  # Calls Parent's method
obj2.show()  # Calls Child's overridden method
