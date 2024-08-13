'''
Rule2
Should
have at least 1
Upper Case All rules must be passe

'''

from sample_registration.uc6 import check_passowrd

def test_valid_cases():

    assert check_passowrd("Prashant@123")==True
    assert check_passowrd("Prashant")==True
    assert check_passowrd("Prashant7774")==True
    assert check_passowrd("Prashant-123")==True
    assert check_passowrd("Prashant$123")==True
    assert check_passowrd("Prashant1212@4@")==True

def test_invalid_cases():

    assert check_passowrd("prashant")==False
    assert check_passowrd("prashan4675")==False
    assert check_passowrd("sdds")==False
