'''
Rule4 Has exactly
1 Special Character All rules must be passed

'''

from sample_registration.uc8 import check_password

def test_valid_cases():

    assert check_password("Prashant@123")==True
    assert check_password("Prashnt@12345")==True


def test_invalid_cases():

    assert check_password("Prashant") == False
    assert check_password("PRAshant") == False
    assert check_password("12345678") == False
    assert check_password("abcdefgh") == False
    assert check_password("ABCDEFGH") == False
    assert check_password("Prashant@@123") == False
    assert check_password("Pr@1234") == False