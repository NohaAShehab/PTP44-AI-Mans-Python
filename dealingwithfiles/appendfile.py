""" write data to the file """
"""
    when you try to open file with mode w
    if file does not exist --> python will try to create it. 
    if file exists ==> python will erase old content 
    as this opens files for writing starting from the beginning of the file
"""

try:
    fileobject = open('info.txt', 'a') # TextIOWrapper
except Exception as e:
    print(e)

else:
    print(fileobject, type(fileobject))
    fileobject.write('We support HAMAS\n')
    fileobject.write('#### We support Abo_Ubida ####\n')

    # fileobject.writelines(['we support hamas', 'Hamas', 'Hamas\n'])
    fileobject.close()

