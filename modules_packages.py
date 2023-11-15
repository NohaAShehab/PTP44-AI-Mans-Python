"""

    every .py file is considered as a module

"""

""" every python module you create --> has an entry point for the main 

 special varaible __name__= "__main__"

"""

coursename = 'Python'


def sayMessage(name=""):
    print(f"----{name}Support Hamas-----")

def sumnum(num1, num2):
    print(num1 + num2)


student_name='Adel'
print("------------------------------------")
if __name__ == '__main__':
    print(coursename)
    sayMessage()


"""
Package -- directory 

"""