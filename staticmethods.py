# class Employee:
#     count = 0  # class variable
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
#         return cls('default', 'default', 1000)
#
#     @classmethod
#     def addEmployees(cls, emp1, emp2):
#         if isinstance(emp1, cls) and isinstance(emp2, cls):
#             newname = emp1.name + emp2.name
#             email = emp1.email + emp2.email
#             salary = emp1.salary + emp2.salary
#             return cls(newname, email, salary)
#
#         raise TypeError("emp1, emp2 must be from Employee")
#
#     @staticmethod  # are helper methods ?
#     def cal_net_salary(salary):
#         print(f"salary = {salary}")
#         return salary * .8
#
#     @staticmethod
#     def formatname(name):
#         return f"{name.upper()}"
#
#
# emp = Employee("noha", "noha@gmail.com")
# print(emp.cal_net_salary(emp.salary))
# print(Employee.cal_net_salary(emp.salary))
# print(emp.name)
# print(Employee.formatname(emp.name))
# print(Employee.cal_net_salary(100000))
# # define function calculate net salary

# def cal_net_salary(salary):
#     return  salary*.8
#
# print(cal_net_salary(10000))
# print(cal_net_salary(emp.salary))


""" check this """


# class Student:
#     instances = {}
#
#     def __init__(self,name):
#         self.name = name
#         Student.instances[self]=name
#
#     @classmethod
#     def get_all_instances(cls):
#         return cls.instances
#
#
#     def __del__(self):
#         Student.instances.pop(self)
#         print("--- object is being deleted ---")
#
#
# student1 = Student('Ahmed')
# print(Student.instances)
#
#
#
# student2 = Student('ali')
#
#
# print(Student.get_all_instances())


""" list --"""
# class Student:
#     instances = []
#     count = 0
#
#     def __init__(self,name):
#         self.name = name
#         Student.instances.append(self.name)
#         self.index = len(Student.instances)-1
#
#     @classmethod
#     def get_all_instances(cls):
#         return cls.instances
#
#     def __del__(self):
#         print(f"--- object destroyed {self.index}")
#         Student.instances.pop(self.index)
#
#
#
# student1 = Student('Ahmed')
# print(Student.instances)
#
# del student1
#
#
# student2= Student("Amina")
# print(Student.instances)
# student3 = Student('ali')
#
# print(Student.get_all_instances())


class Student:
    instances = {}
    count = 0

    def __init__(self,name):
        self.name = name
        Student.instances[self]= self.name

    @classmethod
    def get_all_instances(cls):
        return cls.instances

    def __del__(self):
        print("--- object destroyed ---")
        Student.instances.pop(self)



student1 = Student('Ahmed')
print(Student.instances)

del student1


student2= Student("Amina")
print(Student.instances)

student2= Student("noha")
student3 = Student('ali')

print(Student.get_all_instances())

