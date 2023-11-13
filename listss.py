
"1- define list"
l = []
myl = list()

'2-list can hold different data from different datatypes '
l= ['Ahmed', 'noha', True, 333, 55.55, None,'iti',  ['python', 'pandas'], 'iti']

"3- get len of list "
print(len(l))

'4-access list elements using index '
print(l[3])

'5- list is mutable datatype'
l[3]='Amgad'
print(l)

'6- count element in the list'
print(l.count('iti'))

'7-get index of element'
print(l.index('iti'))

"8- append element to the list ? "
l.append('Ashraf')

'9- insert at certain index'
l.insert(4, 'Hana')

'10- pop element from the list'
# popped_element = l.pop()

"pop element at certain index"
# popped_element = l.pop(7)

"remove element"
l.remove('iti')  # remove the first occurrence of the element.


'sort list --->  > < from the same datatype'
# l.sort()
names= ['Ahmed Mostafa', 'Mohemed Moataz', 'Nadin', 'naira', 'Nawal', 'Amina']
names.sort(reverse=True)  # sort items in the same variable
print(names)

"operations between different lists "
'1- concat'
courses= ['python', 'db', 'ml1']
workshops = ['Git', 'aws', 'testing', 'db']
content = courses + workshops
print(content)

'extend a list ?'
print(courses)
courses.extend(workshops)
print(courses)

'loop over the list ? '
# for item in courses:
#     print(f'item = {item}')

# index=0
# for item in courses:
#     print(f'item = {index}:{item}')
#     index +=1

# enumrate function
#
# for index, item in enumerate(courses):   # generate index for iterable
#     print(f"{index}:{item}")


# for index, char in enumerate("noha"):
#     print(f"{index},{char} ")
#
# "generate list of numbers using range ===? "
# #
# nums = range(1, 10, -2)
# print(nums)
#
# # print(list(nums))
# nums = range(10, 1, -2)
# print(nums)
# for i in nums:
#     print(i)
#
# nums = list(nums)
# # print(nums)

"sort vs reverse"
l= ['Ahmed', 'noha', True, 333, 55.55, None,'iti',  ['python', 'pandas'], 'iti']
l.reverse()
print(l)


"check if element exists in the list "
print('noha'in l)

print("n" in 'noha')


print(list('noha'))