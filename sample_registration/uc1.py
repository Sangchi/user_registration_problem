'''
As a User need to
enter a valid First
Name
- First name starts with Cap and has
minimum 3 characters

'''
import re


def check_name(name):

    pattern=r"^[A-Z][a-z]{2,29}$"

    if re.fullmatch(pattern,name):
        return True
    else:
        return False

def main():

    user_input=input("enter the first name:")
    if check_name(user_input):
        print(f"{user_input}  is valid")

    else:
        print(f"{user_input}  is not valid name")


if __name__=='__main__':
    main()
