print("====== welcome to iti package ====")
""" this is the entry point of the package """
""" content of this file will be exceuted when you just import the package"""


def sayhello(name):
    print(f"Hello {name}")


# register package content in the __init__
from iti.helpers import formatname

print(formatname("   dina -----     "))


