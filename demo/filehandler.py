

def saveUser(userdata):
    userdata= userdata.strip(" \n")
    userdata=f"{userdata}\n"
    try:
        with open('users.txt','a') as usersfile:
            usersfile.write(userdata)
            return True
    except Exception as e:
        return False
