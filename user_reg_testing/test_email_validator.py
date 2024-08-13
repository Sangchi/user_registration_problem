from sample_registration.uc3 import check_email

def test_valid_emails():
    assert check_email("abc.xyz@bl.co.in") == True
    assert check_email("abc@bl.co.in") == True
    assert check_email("abc@bl.co") == True
    assert check_email("abc.xyz@bl.co") == True
    assert check_email("abc@bl.co.in") == True

def test_invalid_emails():
    assert check_email("xyz@bl.co.in") == False
    assert check_email("abc.xyz@co.in") == False
    assert check_email("abc.hii@bl.co.in") == False
    assert check_email("abc.hii@bl.co.edu") ==False
    assert check_email("xyz@bl.in") == False
    assert check_email("abc@co") == False
