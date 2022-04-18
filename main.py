import sys


def greeting(name):
    return f"Hello my name is {name}."


if __name__ == "__main__":
    name = sys.argv[1]
    print(greeting(name))

