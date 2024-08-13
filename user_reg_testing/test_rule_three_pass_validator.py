'''
Rule3  Should
have at least 1
numeric number in
the password - All rules must be passed
Validate that the password contains at least one uppercase letter, one lowercase letter, one digit, and is at least 8 characters long

'''

from sample_registration.uc7 import check_password


def test_valid_cases():

    assert  check_password("Prashant1")==True
    assert check_password("Prashant@123")==True
    assert check_password("PPrashant@1111")==True



def test_invalid_cases():

    assert check_password("Prashant")==False
    assert check_password("PRAshant")==False
    assert check_password("Pr@123") == False
    assert check_password("12345678") == False
    assert check_password("abcdefgh") == False
    assert check_password("ABCDEFGH") == False

