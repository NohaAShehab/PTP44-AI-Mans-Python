

""" abc =--> module contain declarative terms
related to Abstraction in python """
"""ABC  ----> Abstract Base Class"""
from abc import  ABC, abstractmethod


# class Person(ABC):
#     pass
#
# """ this is not an abstract class """
#
# p = Person()

"""to create abstract class must inherit from ABC and have at least one abstract method"""

class Person(ABC):
    @abstractmethod   # call the decorator
    def printPerson(self):
        print("--------")


p = Person()  #TypeError: Can't instantiate abstract class Person with abstract method printPerson

class Student(Person):
    def printPerson(self):
        print("-- implement abstract methods in the base class --")


s = Student()
s.printPerson()
