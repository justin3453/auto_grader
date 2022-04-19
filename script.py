import sys


def greeting(name):
    return f"Hello my name is {name}."


print(greeting(sys.argv[1]))
