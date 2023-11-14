"function ===> accept zero arguments, does nothing "

""" functions with known min and max no of arguments """
# def sayhello():
#     pass
#
# sayhello()
#
# res= sayhello()  # None
# print(res)

""" function and return keyword"""
# def sayhello():
#     return
#
# sayhello()
#
# res= sayhello()  # None
# print(res)

"""===> function do something """
def sayWelcome():
    print('---- Welcome To ITI -----------')

# sayWelcome()
# rr = sayWelcome()

""" function accept arguments """

def sumnum(num1, num2):
    res= num1 + num2
    print(res)

# sumnum(3,5)


"function accept arguments and returns with values"

def getfullname(firstname, lastname):
    fullname = f'{firstname} {lastname}'.title()
    return fullname

#
# myname= getfullname('Ahmed', 'mohamed')
# print(myname)


"function accept default arguments"
""" non default arguments must precede default arguments"""
# def mulnums(num1, num2=10):
#     print(f"num1={num1}, num2={num2}")
#     res = num1 * num2
#     return res, num1, num2  # tuple
#
# # myres = mulnums(30,4)
# myres2= mulnums(7)


""" check this """
print('Ahmed', end='##')
print('ali')
print('ITI')

print(4,5,6,44,sep='--!!--')


"""" ----- functions that accepts variable number of arguments --------------"""


def display_new_items(*items):  # accept zero or more argument
    print(items, type(items))



# display_new_items('Choclate')
# display_new_items('choclate', 'cleaner')
# display_new_items()
#
#
# print()
# print()
# print()
# print('Dina')



""" """


def introduceyourself(**info):  # function accept zero or more keyword arguments
    print(info)

#
# introduceyourself(fname='noha', lname='shehab', city='mansoura')
# introduceyourself()
# introduceyourself(fullname='Nadin Ahmed')
#
#
# temp='We are {mood}'
# print(temp.format(mood='very happy'))

"------------------------- Check this ----------------------"

# def sumnum(num1, num2):
#     num1=str(num1)
#     num2= str(num2)
#     if num1.isdigit() and num2.isdigit():
#         res = num1 + num2
#         print(res)
#     else:
#         print('=== not valid values ===')
#
#
# sumnum(10,30)
# sumnum('noha', 'shehab')
# sumnum(10, 'ahmed')



"check this "

def sumnum(num1 :int, num2:int) -> int :   # for documentation purpose only

    res = num1 + num2
    print(res)



# sumnum(10,30)
# sumnum('noha', 'shehab')
# # sumnum(10, 'ahmed')


""" check this """

print(isinstance('noha', str))
print(isinstance(10 , str))


def sumnum(num1 :int, num2:int) -> int :   # for documentation purpose only
    if isinstance(num1, int) and isinstance(num2, int):
        res = num1 + num2
        print(res)
        return  res
    print('------ num1 and num2 must be integers')

sumnum(10,30)
r= sumnum('noha', 'shehab')
print(r)
sumnum(10, 'ahmed')

