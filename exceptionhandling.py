
# print(course)  #NameError: name 'course' is not defined

# num=int(input("-----dddddddd"))  #ValueError: invalid literal for int() with base 10: 'fdjkshf'

def sumnum(num1, num2):
    res = num1 + num2
    print(res)

# sumnum(10) #TypeError: sumnum() missing 1 required positional argument: 'num2'

# print(5/0) #ZeroDivisionError: division by zero
#
# print=10
# print(10)  #TypeError: 'int' object is not callable

# print("-0-=------------------------")


# try:
#     print(5 / 0)
#
# except:
#     print("--- Error Happened ---")
#
# print("--- here ----")


# def askfornum(message):
#     while True:
#         try:
#             num = int(input(message))
#             return  num
#         except:
#             print("===please enter an integer ====")
#
# print(askfornum("please enter age: "))


# try:
#     print(course)
# except Exception as e:
#     print(e)
""" try and except blocks """

# try:
#     num1=int( input("please enter first number: "))
#     num2= int(input("please enter second number: "))
#     res= num1/num2
#     print(res)
# except TypeError as te:
#     print(f"---- num1 , num2 must be integers : , {te}")
# except ZeroDivisionError as ze:
#     print("==== division by zero is not allowed ==== ")
# except Exception as e:
#     print(e)
#
#
# print("==== after the battle is finished ====  ")
#

""" using the else block """
# try:
#     num1=int( input("please enter first number: "))
#     num2= int(input("please enter second number: "))
#     res= num1/num2
#
# except TypeError as te:
#     print(f"---- num1 , num2 must be integers : , {te}")
# except ZeroDivisionError as ze:
#     print("==== division by zero is not allowed ==== ")
# except Exception as e:
#     print(e)
# else:
#     # this block executed only when there is no exception
#     print(f"==== after the battle is finished ====  {res}")
#

" finally block "
# try:
#     num1=int( input("please enter first number: "))
#     num2= int(input("please enter second number: "))
#     res= num1/num2
#
# except TypeError as te:
#     print(f"---- num1 , num2 must be integers : , {te}")
# except ZeroDivisionError as ze:
#     print("==== division by zero is not allowed ==== ")
# except Exception as e:
#     print(e)
# else:
#     # this block executed only when there is no exception
#     print(f"==== after the battle is finished ====  {res}")
#
# finally:
#     print("--- this block is executed always----")

# print("4567890-=765467890-")

#############################################################


def divnums():
    try:
        num1 = int(input("please enter first number: "))
        num2 = int(input("please enter second number: "))
        res = num1 / num2
        # return "success"

    except TypeError as te:
        print(f"---- num1 , num2 must be integers : , {te}")
    except ZeroDivisionError as ze:
        print("==== division by zero is not allowed ==== ")
    except Exception as e:
        print(e)
    else:
        # this block executed only when there is no exception
        print(f"==== after the battle is finished ====  {res}")
        return  res
    finally:
        """ finally block  precedes  the return """
        print("------------ process complete ==== ")



myres = divnums()
print(myres)









