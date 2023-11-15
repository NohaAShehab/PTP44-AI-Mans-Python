""" write data to the file """
"""
    when you try to open file with mode a
    if file does not exist --> python will try to create it. 
    if file exists ==> python will keep old content 
    as this opens files for writing starting from the end of the file
"""

try:
    fileobject = open('mycv.txt', 'w') # TextIOWrapper
except Exception as e:
    print(e)

else:
    print(fileobject, type(fileobject))
    # fileobject.write('We support HAMAS\n')
    # fileobject.write('#### We support Abo_Ubida ####')

    fileobject.writelines(['we support hamas', 'Hamas', 'Hamas'])
    fileobject.close()

