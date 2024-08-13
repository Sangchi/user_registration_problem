
from sample_registration.uc2 import check_last_name


def test_valid_names():

    assert check_last_name("Chavan")==True
    assert check_last_name("chavan123")==False
    assert check_last_name("Pra")==True
    assert check_last_name("PAwar")==False



def test_invalid_names():

    assert check_last_name("chavan")==False
    assert check_last_name("Pr")==False
    assert check_last_name("PRa")==False




