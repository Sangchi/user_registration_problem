'''
As a User need to
follow pre
-defined
Mobile Format - E.g. 91 9919819801 - Country code follow by space and 10
digit numbe

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

def check_email(input):

    pattern=r"^abc(\.xyz)?@bl\.co(\.in)?$"
    if re.fullmatch(pattern,input):
        return True
    
    else:
        return False
    
def check_mobile_number(input):

    pattern=r"^91(\d{10})$"

    if re.fullmatch(pattern,input):
        return True
    
    else:
        return False

def main():

    user_input1=input("enter the first name:")
    user_input2=input("enter your last name:")
    user_input3=input("enter your email:")
    user_input4=input("enter you mobile number:")

    if check_name(user_input1):
        print(f"{user_input1}  is valid")

    else:
        print(f"{user_input1}  is not valid name")

    if check_last_name(user_input2):
        print(f"{user_input2} is valid name")

    else:
        print(f"{user_input2} is not valid name")

    if check_email(user_input3):
        print(f"{user_input3} is valid Email")

    else:
        print(f"{user_input3} is not valid Email")

    if check_mobile_number(user_input4):
        print(f"{user_input4} is valid mobile number")

    else:
        print(f"{user_input4} is not valid user mobile number")


if __name__=='__main__':
    main()
