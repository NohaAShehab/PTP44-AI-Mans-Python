

for i in range(3):
    password = input("please enter your password: ")
    if password=='abc':
        print('--- logged in successfully')
        break

    print("-----> not valid. please try again ")
else:
    # this block will be executed only if the loop reached its end
    print('==== your account has been blocked')


""" 
    if(){}

"""
name='ahmed'
if name=='ahmed':
    pass  # development branch only
    # print('----hi====')

print("-----")