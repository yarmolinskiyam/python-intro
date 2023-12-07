# from tasks import access_index, sort_sublists, list_to_string, find_index, flatten_list, append_list, random_item, element_exists, smallest_second_index, empty_dict_list, space_separated, add_string
from lists import *

def test_lists_and_strings():
    # Test cases
    assert create_list() == [1, 2, 3]
    assert access_index([1, 2, 3], 1) == 2
    assert slice_list([1, 2, 3, 4, 5], 1, 3) == [2, 3]
    my_list = [1, 2, 3]
    append_element(my_list, 4)
    assert my_list == [1, 2, 3, 4]
    my_list = [1, 2, 3]
    extend_list(my_list, [4, 5])
    assert my_list == [1, 2, 3, 4, 5]
    my_list = [1, 2, 3, 4]
    remove_element(my_list, 3)
    assert my_list == [1, 2, 4]
    my_list = [3, 2, 1]
    sort_list(my_list)
    assert my_list == [1, 2, 3]
