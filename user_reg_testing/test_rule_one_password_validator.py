from sample_registration.uc5 import check_passowrd

def test_valid_cases():

    assert check_passowrd("12345678")==True
    assert check_passowrd("prashant")==True
    assert check_passowrd("Valid1Password")==True
    assert check_passowrd("Another1!Password")==True


def test_invalid_cases():

    assert check_passowrd("123345")==False
    assert check_passowrd("gdasg")==False
    

