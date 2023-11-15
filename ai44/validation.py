

def askforInt(messsage='Please enter a number: '):
    while True:
        num= input(messsage)
        if num.isdigit():
            return int(num)

        print("---- Error---- Please enter valid number number---")


if __name__ == '__main__':
    num= askforInt("Please enter Salary: ")
    print(num, type(num))