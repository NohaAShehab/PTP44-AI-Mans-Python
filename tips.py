

import  json

# name="""
#  shrouq
# """
#
# data = json.dumps(name)
# print(data)

info = {
    "name":"Asmaa Ali",
    "age": 27
}
print(info)
data = json.dumps(info, indent=2)  # string
print(data)

##3 read content from string

mydata = json.dumps('noha')
print(mydata)

res = json.loads(mydata)  # get data from string
print(res)