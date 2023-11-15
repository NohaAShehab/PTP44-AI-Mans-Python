from inputsmodule import askforname
import  time
from demo.filehandler import saveUser
def register():
    username = askforname()
    password = input('please enter your password: ')
    print(username, password)
    id= round(time.time())
    prepared_data=f"{id}:{username}:{password}"
    print(prepared_data)
    saved = saveUser(prepared_data)
    print(saved)


register()

