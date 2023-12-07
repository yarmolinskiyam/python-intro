def create_list():
    # Create a list with elements 1, 2, and 3
    #!v
    my_list = [1, 2, 3]
    #!^
    return my_list

def access_index(lst, index):
    # Return the element at the given index of the list
    #!v
    element = lst[index]
    #!^
    return element

def slice_list(lst, start, end):
    # Return a sliced portion of the list from start to end
    #!v
    sliced_list = lst[start:end]
    #!^
    return sliced_list

def append_element(lst, element):
    # Append the given element to the end of the list
    #!v
    lst.append(element)
    #!^

def extend_list(lst, other_list):
    # Extend the list by adding elements from another list
    #!v
    lst.extend(other_list)
    #!^

def remove_element(lst, element):
    # Remove the first occurrence of the given element from the list
    #!v
    lst.remove(element)
    #!^

def sort_list(lst):
    # Sort the elements of the list in ascending order
    #!v
    lst.sort()
    #!^
