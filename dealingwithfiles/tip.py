
#
# try:
#     with open("info.txt", 'a') as myfile:
#         myfile.write("\n##############")
# except Exception as e:
#     print(e)


# string --> convert to list
info="noha:10:iti"
info_list= info.split(":")
print(info_list)

"list of strings ---> convert them into one string "
mylist=['n','o', 'h', 'a']
name="_".join(mylist)
print(name)