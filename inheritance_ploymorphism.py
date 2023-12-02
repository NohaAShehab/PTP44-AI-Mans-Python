
# class Test(object):
#     pass

# class Person:
#     pass
#
# p= Person()  # call __init__ # special funcion --> generate object address


#
# class Employee(Person):
#     pass


#
# p= Person()
# print(isinstance(p, Person))
# print(isinstance(p,object))

# emp=Employee()
# print(isinstance(emp, Person))
# print(isinstance(emp,object))



""" parent with __init__"""

# class Person:
#     def __init__(self, name):
#         self.name = name
#         print("----- Person created ---")
#
# class Employee(Person):
#     pass
#
#
#
# emp = Employee("ahmed") # call parent constructor and require name.

""" case 2"""

# class Person:
#     def __init__(self, name):
#         self.name = name
#         print("----- Person created ---")
#
# class Employee(Person):
#     def __init__(self, name, email):
#         super().__init__(name)  # if you need to call parent constructor
#         self.email = email
#
#
#
# emp = Employee("ahmed", "ahmed@gmail.com") # call parent constructor and require name.


""" case 3 """
# class Person:
#     def __init__(self, name):
#         self.name = name
#         print("----- Person created ---")
#
#     def printPersonInfo(self):
#         print(f"Person name={self.name}")
#
# class Employee(Person):
#     def __init__(self, name, email):
#         super().__init__(name)  # if you need to call parent constructor
#         self.email = email
#
#
#
# emp = Employee("ahmed", "ahmed@gmail.com")
# emp.printPersonInfo()  # call parent class function



"""case 4"""
# class Person:
#     def __init__(self, name):
#         self.name = name
#         print("----- Person created ---")
#
#     def printPersonInfo(self):
#         print(f"Person name={self.name}")
#
#     """ OVERLOADING IS NOT APPLICABLE EXPLICITLY """
#     # def printPersonInfo(self, message: str):
#     #     print(f"Person {self.name} : {message}")
#
# p1= Person("eee")
# p2= Person("ll")
# print(p1.__le__(p2))
#
# class Employee(Person):
#     def __init__(self, name, email):
#         super().__init__(name)  # if you need to call parent constructor
#         self.email = email
#
#     def printPersonInfo(self):
#         super().printPersonInfo()
#         print(f"====> {self.email}")
#
#
#
# emp = Employee("ahmed", "ahmed@gmail.com")
# emp.printPersonInfo()  # call parent class function

""" mutliple inheritance"""


# class Engineer:
#     pass
#
# class Teacher:
#     pass
#
#
# class Instructor(Engineer, Teacher):
#     pass


# inn = Instructor()
# print(isinstance(inn, Teacher))
# print(isinstance(inn, Engineer))



class Engineer:
    def __init__(self):
        print("I am an Engineer")

class Teacher:
    def __init__(self):
        print("I am a Teacher")


class Instructor(Engineer, Teacher):
    def __init__(self):
        # super().__init__()
        super(Instructor,self).__init__()
        Teacher.__init__(self)
        print("I am an Instructor")


inn = Instructor()