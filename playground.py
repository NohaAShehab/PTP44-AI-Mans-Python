"""
    you need to import value/function from another python module
"""

"--> 1- import all the module "

# import modules_packages

"2- alias module name "
# import  modules_packages as mymodule
#
# mymodule.sayMessage("Noha")
# print(mymodule.coursename)
#
# mymodule.sumnum(2,2)

"""import part of the module """
from modules_packages import sumnum, student_name

sumnum(3,4)

"""------ where is constant in python? """
# print(student_name)
# student_name='Hamdi'


""" import module from package """
# import  ai44.validation
#
# age= ai44.validation.askforInt("please enter your age: ")
# print(age)

""" import packagenmae.modulename """
# import  ai44.validation as validate
#
# age= validate.askforInt("please enter your age: ")
# print(age)

"""
    import tensorflow as ts
    import numpy as np
    import pandas as pd
"""

""" 
    import part of the module 
    from packagename.modulename import functionname
"""

# from ai44.validation import  askforInt
# print(askforInt('please enter salary: '))
""""""

# import iti
# from iti import sayhello
# sayhello("Ahmed")


# from iti.helpers import formatname
# print(formatname("         noha        "))


# from iti import formatname
#
# print(formatname("         noha        "))


import iti  # iti is package name
