def add():
    print("Result 1 is: ", __name__)


def sub():
    print("Result 2 is: ", __name__)


def main():
    print("In main")
    add()
    sub()


if __name__ == '__main__':
    main()
