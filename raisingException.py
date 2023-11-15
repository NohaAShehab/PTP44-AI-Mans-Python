

def sumnums(num1, num2):
    if not(isinstance(num1,int) and isinstance(num2, int)):
        raise  TypeError('num1 and num2 must be Integer')
    res = num1 +num2
    return res

print(sumnums(10,20))

print(sumnums(40, 'iti'))