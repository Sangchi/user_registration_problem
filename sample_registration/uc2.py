'''
As a User need to
enter
a valid Last
Name - Last name starts with Cap and has
minimum 3 character

'''
import re


def check_last_name(input):

    pattern=r"^[A-Z][a-z]{2,29}$"

    if re.fullmatch(pattern,input):
        return True
    
    else:
        return False

def main():
    user_input=input("enter your last name:")
    if check_last_name(user_input):
        print(f"{user_input} is valid name")

    else:
        print(f"{user_input} is not valid name")


if __name__=='__main__':
    main()