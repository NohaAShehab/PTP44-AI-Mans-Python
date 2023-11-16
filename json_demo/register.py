" buitlin imports"
import  time
""" external libraries imports """

""" user defined modules """
from  json_demo.json_handler import save_student, get_all_students

def register():
    email=input("please enter email: ")
    password = input("please enter password: ")
    print(email, password)
    # prepare data to be saved
    id = round(time.time())
    data = {
        "id":id,
        "email":email,
        'password': password
    }
    res=save_student(data)

    return res





def mainmenu():
    while True:
        choice = input("please enter r for regiser , l for list , e exit")
        if choice=='r':
            register()
        elif choice=='l':
            print(get_all_students())
        elif choice=='e':
            exit()


if __name__ == '__main__':
    mainmenu()