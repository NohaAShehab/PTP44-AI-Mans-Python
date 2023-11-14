""" variable defined inside the script"""
course = 'python'  # define variable in the global scope of the script
""" you can use it anywhere in the script"""

# print(course)


"variable defined inside the function "

# def sayhello():
#     "any variable defined in the function --> localscope "
#     "can be accessed only inside the function "
#     name=input('please enter name: ')  # local
#     print(f'{name} supports HAMAS')
#
#
# sayhello()
# print("------")
# # print(name)


# read global variable from inside function

course='python'
# def printCourse():
#     print(f'course={course}')
#
# printCourse()

"modify global variable from inside function"
# course='python'
# def modifyCourse():
#     global course # please don't create new object ---> use the global one
#     course='Machine learning'
#     print(f"from inside the function course={course}")
#
#
# modifyCourse()
# print(course)

""" function inside function """

# def courseinfo():
#     coursename='Python'
#     def formatCourse():
#         "read local variable of the function from inside inner function"
#         print(coursename.upper())
#
#     print(coursename)
#     formatCourse()


# courseinfo()

#
#
# def courseinfo():
#     coursename='Python'
#     def formatCourse():
#         "read local variable of the function from inside inner function"
#         print(coursename.upper())
#     def updateCourse():
#         coursename=input('please enter course: ') # new local variab;
#         print(coursename)
#
#     updateCourse()
#     print(coursename)
#
# courseinfo()















def courseinfo():
    coursename='Python'
    def formatCourse():
        "read local variable of the function from inside inner function"
        print(coursename.upper())
    def updateCourse():
        nonlocal coursename  # please use the variable in the parent function.
        # and don't create new one
        coursename=input('please enter course: ') # new local variab;
        print(coursename)

    updateCourse()
    print(coursename)

courseinfo()





for i in range(10):
    print(i)


print(i)