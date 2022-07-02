#Python Screening Assignment

# 1.
 # Python program to read & replace text in the file with logging & exception handling.

import logging as lg
lg.basicConfig(filename = 'logger.log' , level = lg.ERROR , format = "%(asctime)s %(message)s")

def assignment():
    try:
        with open("example.txt", "w") as file :
            file.write("This is a placement assignment")
        with open("example.txt", "r+") as file :
            content = file.read()
            replacement = content.replace("placement", "screening")
            file.truncate(0)
            nl = ("\n")
            file.write(nl + replacement)
        print("Original file content-", content)
        print("Replaced file content-", replacement)

    except Exception as e:
        lg.exception(e)
        print("* An error has occurred in the file or program *")

assignment()
print()


# 2.
 # An abstract class is a great choice if you are accounting the inheritance concept
 # because it provides the common base class implementation to the derived classes.
# defining a abstract class.
from abc import ABC, abstractmethod       # importing abstract base class & abstract method from abc module.

class object(ABC):                        # we can't instantiate the object class
    @abstractmethod                       # because it is an abstract class.
    def area(self): pass

    @abstractmethod                       # decorator should be placed under atleast one method.
    def perimeter(self): pass

class Rectangle(object):                  # we need to provide the implimentation of
    def __init__(self , length , width):  # area & perimeter method in the subclass.
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2*(self.__length + self.__width)

rec = Rectangle(5 ,4)
print("Area of rectangle-" ,rec.area())
print("Perimeter of rectangle-" ,rec.perimeter())
print()


 # multiple inheritance occurs when a class inherits from more than one base class.
# defining a multiple inheritance.
class Person():                       # Person class which will be inherited.
    def activity(self):
        print("Activity- working,playing,gardening")
    def skills(self):
        print("Skills- programming,cooking")

class Child(Person):                  # Child class is inherited from Person class
    def inheriting(self):
        Person.activity()
        Person.skills()
        print("MULTIPLE INHERITANCE")

child = Child()
child.activity()
child.skills()
print()


 # decorator is a function that helps to add some additional functionalities to an already defined function.
# defining a decorator.
def decorator(fun):
    def inside(x, y):
        if y == 0:
            print("Can't divide by 0")
            return
        fun(x, y)
    return inside

@decorator                            # calling the decorator function
def div(a, b):
    return a / b

print(div(10, 0))
