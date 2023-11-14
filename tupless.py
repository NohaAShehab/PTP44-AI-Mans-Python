# 
"tuple like tuple but it is one of the immutable non-primitive datatypes in python --> "
"1- define tuple"
t = ()
myt = tuple()
# 
'2-tuple can hold different data from different datatypes '
t= ('Ahmed', 'noha', True, 333, 55.55, None,'iti',
    ['python', 'pandas'], 'iti', ('ahmed', 'mohamed'))
# 
"3- get len of tuple "
print(len(t))
# 
'4-access tuple elements using index '
print(t[3])
# 
'5- tuple is immutable datatype'
# t[3]='Amgad'  #'tuple' object does not support item assignment
# print(t)
# 
'6- count element in the tuple'
print(t.count('iti'))
# 
'7-get index of element'
print(t.index('iti'))
# 




"operations between different tuples "
'1- concat'
courses= ('python', 'db', 'ml1')
workshops = ('Git', 'aws', 'testing', 'db')
content = courses + workshops
print(content)


'loop over the tuple ? '
for item in courses:
    print(f'item = {item}')
# 
index=0
for item in courses:
    print(f'item = {index}:{item}')
    index +=1

# enumrate function
#
for index, item in enumerate(courses):   # generate index for iterable
    print(f"{index}:{item}")
# 

"generate tuple of numbers using range ===? "
#
nums = range(1, 10, 2)   #range object
print(nums)
# #
print(tuple(nums))



"check if element exists in the tuple "
print('noha'in t)

"cast list to tuple and vice versa? "
names = ['Shrouk', "Nada", "hamdy", "Ahmed"]
names = tuple(names)
print(names)

names=list(names)
print(names)


# tuple of one item
# students = tuple(['Adel'])
#
# mystds = ("Adel",)
name='nada'
ll=['ss','sss']
content=("Ahmed", "Mohamed", ["python", 'DL', "NLP"], name, ll)
print(content[2][1])
content[2].append('AWS')
print(content)
name='Nada AbdelFatah'
print(content)
ll.append("ttt")
print(content)