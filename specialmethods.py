

# class Employee(object):
#
#     def __init__(self,name, email, salary):
#         self.name=name
#         self._email= email
#         self.__salary= salary
#
#     def __str__(self):
#         # must return with string
#         return f"{self.name}"
#
#     def __repr__(self):
#         # must return with string
#         return f"Employee(name={self.name}, email={self._email}, salary={self.__salary})"
#
#     # allow object to be called
#     def __call__(self, *args, **kwargs):
#         print("--- object is being called -----")
#
#     def __len__(self):
#         # must return with number
#         return  len(self.__dict__)
#
#
#     def __add__(self, other):
#         if type(other)==type(self):
#             return "added"
#         raise  ValueError("----")
#
#
#
#
# emp = Employee("ahmed", 'ahmed@gmail.com', 45567765)
# print(emp)
# print(emp.__dict__)
# print(emp.__repr__())  # return object representation
#
# emp()
# print(len(emp))
#
# emp2 = Employee("fff", 'fff', 3333)
# print(emp + emp2)
#
# print(emp + 10)

"-----------------------------------"


class Employee:
    gi = ['name', 'email', 'salary']
    def __init__(self, name, email, salary):
        self.name= name
        self.email= email
        self.salary= salary


e = Employee("hamed", "<EMAIL>", 444444)
e.city = 'test'