

"""

    file
        1-open file ===> (mode 'r', 'w' , 'a')
        open(filename, mode) # TextIOWrapper -->
        2- do operation  (read, write )
        3- close the file

"""

"""1- read data from file  into one string """

# try:
#     fileobject = open('students.txt', 'r') # TextIOWrapper
# except Exception as e:
#     print(e)
#
# else:
#     print(fileobject, type(fileobject))
#     # to read content
#     # use read function load file content into one string
#     data = fileobject.read()
#     print(data, type(data))
#     fileobject.close()
#
#


"""read data line by line """
try:
    fileobject = open('students.txt', 'r') # TextIOWrapper
except Exception as e:
    print(e)

else:
    print(fileobject, type(fileobject))
    # for line in fileobject:
    #     print(f"line={line}")

    lines = fileobject.readlines()  # read file content line by line in a list
    print(lines)
    fileobject.seek(10)
    alldata= fileobject.read() # string
    print(alldata)
    fileobject.close()
