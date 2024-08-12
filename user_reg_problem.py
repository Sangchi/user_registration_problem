'''
As a User need to
enter
a valid Last
Name - Last name starts with Cap and has
minimum 3 character

'''
import re


def check_name(name):

    pattern=r"^[A-Z][a-z]{2,29}$"

    if re.fullmatch(pattern,name):
        return True
    else:
        return False


def check_last_name(input):

    pattern=r"^[A-Z][a-z]{2,29}$"

    if re.fullmatch(pattern,input):
        return True

    else:
        return False

def main():

    user_input1=input("enter the first name:")
    user_input2=input("enter your last name:")
    user_input3=input("enter your email:")

    if check_name(user_input1):
        print(f"{user_input1}  is valid")

    else:
        print(f"{user_input1}  is not valid name")

    if check_last_name(user_input2):
        print(f"{user_input2} is valid name")

    else:
        print(f"{user_input2} is not valid name")


if __name__=='__main__':
    main()


