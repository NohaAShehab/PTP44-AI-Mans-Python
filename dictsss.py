"""
 mutable datatype
 comma seperated key:value pair
 doesn't allow key duplication
 from python 3.7 --> dict ---> ordered datatype

"""

"1- define a dict "
d=  {}
myd= dict()

myd2=dict([('course',['python', 'pandas']), ('instructor', 'noha'), ('info', {'name':"Ahmed"})])

myd2['course']='pandas'

"2- dict contains info "
info = {
    "name":"noha", "work":"iti", 'age':31, "name":"Noha Shehab"
}
print(info)

"3- access dict parts using key "
print(info['name'])

"4- update dict content"
info['work']='Information Technology Institute'
print(info)
info['city']='Mansoura'
print(info)

"5- get len of dict "
print(len(info))

"check if element exists in the dict"
print(31 in info)  # check if values exists in the keys

"get dict keys"
keys = info.keys()
print(keys, type(keys))
#
# for k in keys:
#     print(k)

# keys =list(keys)


"get dict keys"
values = info.values()
print(values, type(values))

print(31 in info.values())


"loop over the dict"
for item in info:
    print(f"item={item}, {info[item]}")

"get items of the dict "
d_items = info.items()
print(d_items, type(d_items))

d_items = list(d_items)

for k, v in info.items():
    print(f"{k}:{v}")

"update dict ? "

dataaa= {"track":"AI", "intake":44, "branch":"Mansoura"}

courses = {"essentials":['c', 'c++'],'programming':"Python", 'core':['ml1', 'ml2']}
# print(courses)
#
#
#
# dataaa.update(courses)
#
# print(dataaa)

courses_list=list(courses)
print(courses_list)

########## 2 functions

# courses.clear()
# print(courses)
"""pop key from dict """
popped_value=courses.pop("essentials")
print(popped_value)

# nadin_suggestion={('a', "b"):"red"}
# print(nadin_suggestion[('a', 'b')])


############################