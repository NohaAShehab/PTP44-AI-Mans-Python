

def askforname(message='please enter your name:'):
    while True:
        name= input(message)
        if name.isalpha():
            return name
        print("---please try again---")