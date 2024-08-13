from sample_registration.uc4 import check_mobile_number

def test_valid_input():

    assert check_mobile_number("917774859318")==True


def test_invalid():

    assert check_mobile_number("91777abc123")==False
    assert check_mobile_number("1234567890")==False
    assert check_mobile_number("1234567")==False
    assert check_mobile_number("123456789012345")==False
    assert check_mobile_number("123-456-7890")==False
    assert check_mobile_number("91123-456-78")==False