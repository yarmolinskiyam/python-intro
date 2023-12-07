from dictionaries import *

def test_dict():
    # Test cases
    assert create_dictionary() == {"apple": 1, "banana": 2, "orange": 3}
    assert access_value({"apple": 1, "banana": 2, "orange": 3}, "apple") == 1

    my_dict = {"apple": 1, "banana": 2, "orange": 3}
    add_key_value(my_dict, "kiwi", 4)
    assert my_dict == {"apple": 1, "banana": 2, "orange": 3, "kiwi": 4}

    my_dict = {"apple": 1, "banana": 2, "orange": 3}
    remove_key_value(my_dict, "orange")
    assert my_dict == {"apple": 1, "banana": 2}

    assert check_key_exists({"apple": 1, "banana": 2, "orange": 3}, "apple") == True
    assert check_key_exists({"apple": 1, "banana": 2, "orange": 3}, "kiwi") == False
