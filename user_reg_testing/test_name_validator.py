from sample_registration.uc1 import check_name

def test_valid_names():
    assert check_name("John") == True
    assert check_name("Alice") == True
    assert check_name("Xander") == True
    assert check_name("O'Connor") == False
    assert check_name("Yvonne") == True
    assert check_name("YYone")==False
    assert check_name("Prshant1234")==False

def test_invalid_names():
    assert check_name("john") == False  # starts with lowercase
    assert check_name("Jo") == False    # too short
    assert check_name("O'Conner") == False # valid as per updated pattern
    assert check_name("Anne@Marie") == False  # contains invalid character '@'
    assert check_name("Anne-Marie-") == False  # ends with invalid character '-'
    assert check_name("1234") == False  # only digits
    assert check_name("A@") == False  # invalid character '@'
    assert check_name("O'Connor-Smith") == False  # hyphen not allowed in the middle


