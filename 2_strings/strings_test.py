from strings import *

def test_strings():
    # Test cases
    assert create_string() == "Hello, world!"
    assert access_char("Hello, world!", 7) == 'w'
    assert slice_string("Hello, world!", 1, 5) == "ello"
    assert concatenate_strings("Hello, world!", " How are you?") == "Hello, world! How are you?"
    assert uppercase_string("Hello, world!") == "HELLO, WORLD!"
    assert lowercase_string("Hello, world!") == "hello, world!"
