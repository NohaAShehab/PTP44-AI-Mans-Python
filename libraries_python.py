

""" built in libraries in python """

"1- math"

import math
# print(math.pi)
#
# print(math.cos(30))
#
# print(math.factorial(5))
# print(math.fabs(-5))

"time "
# import  time
#
# print(round(time.time()))


"os"
import  os
print(os.getcwd())
# print(os.path.join('/test', '/ttt'))
# print(os.mkdir("newdir"))
os.system('ls -l')
print(os.getcwd())
# os.chdir('/home/noha')
print(os.getcwd())
print(os.getlogin())
# print(os.system('touch myfile.txt'))
# os.system('sudo touch /home/myfile.txt')
# os.system('chmod 777 myfile.txt')
# print(os.system('ls -l'))
print()
"sys"
import sys
# print(sys.platform)
# sys.exit()


import re

# def is_valid_email(email):
#     pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
#     m= re.match(pattern, email)
#     print(m)
#     return m
#
# # Example usage:
# email_to_check = 'noha@gmail.comn'
# res = is_valid_email(email_to_check)
# if res:
#     print(f"{email_to_check} is a valid email address.")
# else:
#     print(f"{email_to_check} is not a valid email address.")




regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
#
email = '44   444   noha@gmail.com noha@gmail.com'

res=  re.search(regex, email)  # return with match object if the part of the string statisfy pattern
print(res)
#
# res=  re.fullmatch(regex, email)  # return with match object if the whole  the string statisfy pattern
# print(res)



# Define a simple pattern
pattern = r'\b\d{3}-\d{2}-\d{4}\b'  # This pattern matches a social security number

# Example string
# text = "John's SSN is 123-45-6789   123-45-6789"

# Use re.search() to find a match
# match = re.search(pattern, text)
# print(match)
# Check if a match was found
# if match:
#     ssn = match.group()  # Get the matched string
#     print(f"Social Security Number found: {ssn}")
# else:
#     print("No Social Security Number found.")