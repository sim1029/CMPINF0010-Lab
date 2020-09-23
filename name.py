#!/bin/python3

def main():
    name = input("Enter your first name: ")
    hobby = input("Enter your favorite hobby: ")
    food = input("Enter your favorite food: ")

    desc = ("{0}'s favorite hobby is {1} and their favorite food is {2}. "
            "Aren't they awesome?!").format(name, hobby, food)

    print(desc)


if __name__ == '__main__':
    main()
