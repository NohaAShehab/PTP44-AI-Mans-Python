# emp = {
#     "name" :"omar",
#     "email": "omar@gmail.com",
#     'salary' :1000
# }
#
# emp2= {
#     "empname" :"dina",
#     "emp_email" :"dina@gmail.com",
#     "salary": 4000
# }

# def printEmpInfo(emp):
#     print(f"name={emp['name']}, email={emp['email']}")
#
# printEmpInfo(emp2)


"""define new datatype ---> user defined datatype
    customized datatype --->
    define new structure --> uniform structure for the instances
    -objects -

"""
# l = []
# l.append("rrr")

"""1- to define class --> blueprint 
---> new customized userdefined datatype"""
#
# class Employee:
#     pass
#
#
# class Developer(object):
#     pass


""" take object from the class """
"object factory"

"python is loosely dynamically lang."
# class Employee:
#     pass
#
#
# emp = Employee()  # instance of class ? contains data --> implement func.
# print(emp)
# # emp ===> type ==> object / instance =Employee
# emp.name = 'Ali'
# emp.salary = 2000
#
#
# emp2=  Employee()
# emp2.empname='Naira'
# emp2.empsalary = 5000

"customize object creation --->> constructor "
# class Employee:
#     def __init__(self):
#         """ when you create an object , __init__ reserve
#         new address in the memory ? self --> """
#         print(f"--- the object is being created now \n"
#               f", {self}")
#
#
# emp = Employee()
# print(emp)
# emp.name='Roaa'
# print("-----------------------")
# emp2 =Employee()
# print(emp2)
# emp2.name='Ahmed'

""" customize object creation """
# class Employee:
#     def __init__(self):
#         self.name='Ahmed'
#         self.email='ahmed@gmail.com'
#         self.salary=1000
#
# emp = Employee()
# print(emp)
# print(emp.name)
# emp.name='ali'
# print(emp.name)
#
# emp2 = Employee()


# class Employee:
#     def __init__(self,name, email, salary):
#         # to define object properties ---> inside __init__, constructor
#         """ name, email, salary --> instance variables
#             their values -->depend on caller instance
#         """
#         self.name=name
#         self.email=email
#         self.salary=salary
#
# emp = Employee("ahmed",'ahmed@gmail.com', 3000)
# print(emp.name)
# emp2 = Employee("roaa", "Roaa@gmail.com", 4000)
# print(emp2.name)


""" constructor with default values """

# class Employee:
#     def __init__(self, name, email, salary=5000):
#         # to define object properties ---> inside __init__, constructor
#         """ name, email, salary --> instance variables
#             their values -->depend on caller instance
#         """
#         self.name = name
#         self.email = email
#         self.salary = salary
#
#
# emp = Employee("ahmed", 'ahmed@gmail.com', 3000)
# print(emp.name)
# emp2 = Employee("roaa", "Roaa@gmail.com", 4000)
# print(emp2.name)
# emp3 = Employee("Nada", 'nada@gmail.com')
# print(emp3.salary)
# emp3.city = 'Mansoura'

""" =====  instance methods """
# class Employee:
#     def __init__(self, name, email, salary=5000):
#         """ name, email, salary --> instance variables"""
#         self.name = name
#         self.email = email
#         self.salary = salary
#
#     # define instance methods ?
#
#     def printEmpInfo(self, message='Hi'):  # instance method --> current caller instance
#         print(f"{message}: "
#               f"name={self.name}, email={self.email}, salary={self.salary}")
#
#
# emp = Employee("ahmed", 'ahmed@gmail.com', 3000)
# emp.printEmpInfo()
# emp2 = Employee("roaa", "Roaa@gmail.com", 4000)
# emp2.printEmpInfo()


""" count objects taken from the class ? class variable """

# class Employee:
#     count = 0  # class variable
#     # property depends on the class on the instance
#     def __init__(self, name, email, salary=5000):
#         self.name = name
#         self.email = email
#         self.salary = salary
#         # self.__class__.count +=1
#         Employee.count +=1
#
#
#     def printEmpInfo(self, message='Hi'):  # instance method --> current caller instance
#         print(f"{message}: "
#               f"name={self.name}, email={self.email}, salary={self.salary}")
#
#
# print(Employee.count)
# emp= Employee("Ahmed","ahmed@gmail.com", 4000)
# print(Employee.count)
# print(emp.count)
#
# """ class variable --> shared property between the instances of the class"""
# Employee.nationality='Egyptian'
# #
# #
# emp2= Employee("ali","ali@gmail.com", 4000)
# print(emp2.count)


""" class method """

# class Employee:
#     count = 0  # class variable
#     def __init__(self, name, email, salary=5000):
#         self.name = name
#         self.email = email
#         self.salary = salary
#         # self.__class__.count +=1
#         Employee.count +=1
#
#     def printEmpInfo(self, message='Hi'):  # instance method --> current caller instance
#         print(f"{message}: "
#               f"name={self.name}, email={self.email}, salary={self.salary}")
#
#     # define behaviour related to the class not the instance
#     # class method ?
#
#     # def printEmpCount(self):  # this function will be called with instance
#     #     print(f"No of Employees till now = {Employee.count}")
#
#     """ create class method --> behaviour depends on the class """
#     @classmethod # the below method depends on the class not the instance
#     def printEmpCount(cls):  # make the first parameter of the function
#         # represent the class
#         print(cls)
#         print(f"No of Employees: {Employee.count}")
#         print(f"No of Employees: {cls.count}")
#
#
# emp1= Employee("ahmed", "ahmed@gmail.com", 10000)
#
# Employee.printEmpCount()  # this class method ---?
# #call it using classname
#
# print(Employee.count)
#

""" check this """

# class Employee:
#     count = 0  # class variable
#
#
#     def __init__(self, name, email, salary=5000):
#         self.name = name
#         self.email = email
#         self.salary = salary
#         # self.__class__.count +=1
#         Employee.count += 1
#
#     def printEmpInfo(self, message='Hi'):  # instance method --> current caller instance
#         print(f"{message}: "
#               f"name={self.name}, email={self.email}, salary={self.salary}")
#
#     """ create class method --> behaviour depends on the class """
#
#     @classmethod  # the below method depends on the class not the instance
#     def printEmpCount(cls):  # make the first parameter of the function
#         # represent the class
#         print(cls)
#         print(f"No of Employees: {Employee.count}")
#         print(f"No of Employees: {cls.count}")
#
#     # use class method as object factory
#     @classmethod
#     def createDefaultEmployee(cls):
#         # return  Employee('default', 'default', 1000)
#         return  cls('default', 'default', 1000)
#
#     @classmethod
#     def addEmployees(cls, emp1 , emp2):
#         if isinstance(emp1, cls) and isinstance(emp2, cls):
#             newname= emp1.name + emp2.name
#             email = emp1.email + emp2.email
#             salary = emp1.salary + emp2.salary
#             return  cls(newname, email, salary)
#
#         raise TypeError("emp1, emp2 must be from Employee")
#
# # operator overloading + - -> return new object form the class
# # operator overloading  --> class Complex ?
# Employee.printEmpCount()  # this class method ---?
#
# emp1 = Employee.createDefaultEmployee()
# emp2= Employee('test','test@gmail', 1000)
# emp3 = Employee.addEmployees(emp1, emp2)
# emp3.printEmpInfo()


# task --> object oriented
# method create project ? --> instance method
# method list all project ---> class method


""" destructor method """


class Employee:
    count = 0  # class variable

    def __init__(self, name, email, salary=5000):
        self.name = name
        self.email = email
        self.salary = salary
        # self.__class__.count +=1
        Employee.count += 1

    def printEmpInfo(self, message='Hi'):  # instance method --> current caller instance
        print(f"{message}: "
              f"name={self.name}, email={self.email}, salary={self.salary}")

    """ create class method --> behaviour depends on the class """

    @classmethod  # the below method depends on the class not the instance
    def printEmpCount(cls):  # make the first parameter of the function
        # represent the class
        print(cls)
        print(f"No of Employees: {Employee.count}")
        print(f"No of Employees: {cls.count}")

    # use class method as object factory
    @classmethod
    def createDefaultEmployee(cls):
        # return  Employee('default', 'default', 1000)
        return cls('default', 'default', 1000)

    @classmethod
    def addEmployees(cls, emp1, emp2):
        if isinstance(emp1, cls) and isinstance(emp2, cls):
            newname = emp1.name + emp2.name
            email = emp1.email + emp2.email
            salary = emp1.salary + emp2.salary
            return cls(newname, email, salary)

        raise TypeError("emp1, emp2 must be from Employee")

    # define destructor inside class
    def __del__(self):
        #this function will be called either when you delete object
        # or the execution finished
        print(f"---- object is being deleted {self.name} -----")


emp = Employee.createDefaultEmployee()
print(emp)

emp2 = Employee("ahmed", "ahmed@gmail.com", 2000)
emp3 = Employee.addEmployees(emp, emp2)
print("----Dina ----")
del emp2
print("------Ali----")
emp3.printEmpInfo()

print("------------------------------------")
print("------------- Hi shoruk ----")