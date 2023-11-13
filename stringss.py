

"1- define string"
name='information technology Institute'
"2- access strings parts using index starts from 0"
print(name[0])
print(name[2:8])
print(name[4:])
print(name[::])
print(name[::-1])  # revese string

"3- get len of the string "
print(len(name))

"4- count char occurrence in the string"
print(name.count('i'))  # case sensitive

"5- get index of char "
print(name.index('i'))  # get the first occurrence of the char


"6- string is immutable data type "
# name[10]='ffff'

"""apply operation on the string --> return with new string """
"""7- format string"""
message = 'we support Hamas'

# these function must return with new string
print(message.upper())
print(message.lower())
print(message.capitalize())
print(message.title())

" format string using format function"
no_students=  22
leader= 'Ahmed'

"string concatenation"
# message = 'we have '+ str(no_students) + " students in ai track , leader name is "+ leader
# print(message)

"format function"
# temp =  'we have {0} students in a i track, leader name is {1}'
# print(temp.format(no_students, leader))
#
#
temp =  'we have {totalnumber} students in a i track, leader name is {leadername}'
# print(temp.format(leadername=leader, totalnumber=no_students))

"""f-format string """
# creating the string depends on existence of the variables in the memory
temp =  f'we have {no_students} students in ai track, leader name is {leader}'
print(temp)


"""strip string """
message = '         My name is Noha                        @    '
"strip white spaces from the beginning and the end of the string "
print(message)
# print(message.strip())
# print(message.lstrip())
# print(message.rstrip())
print(message.strip(" @M"))
# print(message.lstrip())
# print(message.rstrip())

"""string replace ---> replace string with another string """
message= 'we support Hamas  a   a   aa  aaa'
print(message.replace('a', '@'))
print(message.replace('a', 'a', 3))


""" string interpolation"""
fname='Noha'
midname='AbdelHady'
lname='Shehab'

# fullname=fname + midname + midname +lname
fullname=fname + midname +lname
print(fullname)


"""ask user to enter string """
mood = input("Please let me know how are you now! : ")  # always returns with String
print(mood, type(mood))

""" examine string content """
print(mood.isdigit())  # return True only if the string consists of digits 0-->9 only
print(mood.isalpha())  # return True only if the string consists of alphas a-->z
print(mood.isupper())



# age= int(input('please enter your age: '))
# print(age, type(age))

# age= input('please enter your age: ')
# if age.isdigit():
#     age= int(age)
#     print(age, type(age))

# age= float(input('please enter your age: '))




