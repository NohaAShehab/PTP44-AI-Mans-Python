
"""remove duplicate elements, no index , un ordered datatype
allow  adding only immutable datatypes
"""
"1- define set "
s = set()
mys = {"Ahmed", "iti", "Ali", "iti", "Shrouk", "nadin", 'Mohamed Moataz', 'iti', 10, 33.3, True}
print(mys)


"2- get len"
print(len(mys))

"3- immutable or mutable ? "
mys.add("Nawal")
print(mys)

# "4- remove element from the set ?"
# mys.remove("Ahmed")  # specific element
# print(mys)
# "5- pop element"
# popped_element= mys.pop() # remove random element
# print(popped_element)

"6- check element exists or not ? "
print('Ahmed' in mys)

"7-update set "
mys2={{'test', 'mysqll'}, ("ml2", 'nlp'), True}

mys.update(mys2)
print(mys)