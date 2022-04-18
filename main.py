import sys


def greeting(name):
    return f"Hello my name is {name}."


name = sys.argv[1]
print(greeting(name))

