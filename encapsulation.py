# class Employee:
#     def __init__(self ,name, email, salary):
#         self.name = name  # public
#         self._email = email  # protected
#         self.__salary = salary
#
#     def printEmployee(self):
#         print(f"name={self.name},email={self._email},salary={self.__salary}")
#
#
# emp= Employee('Ahmed', "ahmed@gmail.com", 100000)
# print(emp.name)
# print(emp._email) # Ethically don't do this.
# # print(emp.__salary)  # Employee' object has no attribute '__salary'
# print(emp._Employee__salary)  # Ethically don't do this.
#
#
# """ special method in oop classes in python"""
# # print(emp.__dict__)  # represent object properties in form  of dict
# """ loosely dynamically typed lang. """
# emp.__city ='mansoura'
# print(emp.__city)


""" get value of salary """
# class Employee:
#     def __init__(self ,name, email, salary):
#         self.name = name  # public
#         self._email = email  # protected
#         self.__salary = salary  #private
#
#     def printEmployee(self):
#         print(f"name={self.name},email={self._email},salary={self.__salary}")
#
#     def getSalary(self):
#         return self.__salary
#
#     def setSalary(self, salary):
#         if isinstance(salary , int) or isinstance(salary, float):
#             self.__salary = salary
#         else:
#             raise ValueError("Salary must be int or float ")
#
# employee = Employee("Dina", 'dina@gmail.com', 1000000)
# print(employee.getSalary())
# # employee.setSalary(5634567865432)
# employee.setSalary("iti")

""" check this """
# class Employee:
#     def __init__(self ,name, email, salary):
#         self.name = name  # public
#         self._email = email  # protected
#         self.setSalary(salary)
#
#     def printEmployee(self):
#         print(f"name={self.name},email={self._email},salary={self.__salary}")
#
#     """ apply operation on __salary property """
#     def getSalary(self):
#         return self.__salary*.8
#
#     def setSalary(self, salary):
#         if isinstance(salary , int) or isinstance(salary, float):
#             self.__salary = salary
#         else:
#             raise ValueError("Salary must be int or float ")
#
# employee = Employee("Dina", 'dina@gmail.com', "iti")
# print(employee.getSalary())


""" introduct property decorator """


# class Employee:
#     def __init__(self, name, email, salary):
#         self.name = name  # public
#         self._email = email  # protected
#         self.setSalary(salary)
#
#     def printEmployee(self):
#         print(f"name={self.name},email={self._email},salary={self.__salary}")
#
#     """ apply operation on __salary property """
#
#     @property
#     def salary(self):
#         return self.__salary * .8
#
#
#     @salary.setter
#     def salary(self, salary):
#         if isinstance(salary, int) or isinstance(salary, float):
#             self.__salary = salary
#         else:
#             raise ValueError("Salary must be int or float ")
#     def setSalary(self, salary):
#         if isinstance(salary, int) or isinstance(salary, float):
#             self.__salary = salary
#         else:
#             raise ValueError("Salary must be int or float ")
#
#
# employee = Employee("Dina", 'dina@gmail.com', 20000)
# print(employee.salary)
# print(employee.__dict__)
# employee.name='test'
# employee.salary=10000000
# print("--------------------")

"""-------------------"""
class Employee:
    def __init__(self, name, email, salary):
        self.name = name  # public
        self._email = email  # protected
        # self.__salary = salary
        self.salary =salary



    def printEmployee(self):
        print(f"name={self.name},email={self._email},salary={self.__salary}")

    @property
    def salary(self):
        return self.__salary * .8

    @salary.setter
    def salary(self, salary):
        if isinstance(salary, int) or isinstance(salary, float):
            self.__salary = salary
        else:
            raise ValueError("Salary must be int or float ")


emp = Employee("Shrouq", "sh@gmail.com", 66666)
# print(emp.salary)
# emp.salary = 'ffffff'
print(emp.salary) # call property getter