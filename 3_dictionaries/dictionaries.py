def create_dictionary():
    # Create a dictionary with the keys "apple", "banana", and "orange" and their respective values (1, 2, and 3)
    #!v
    my_dict = {"apple": 1, "banana": 2, "orange": 3}
    #!^
    return my_dict

def access_value(dictionary, key):
    # Return the value associated with the given key in the dictionary
    #!v
    value = dictionary[key]
    #!^
    return value

def add_key_value(dictionary, key, value):
    # Add a key-value pair to the dictionary
    #!v
    dictionary[key] = value
    #!^

def remove_key_value(dictionary, key):
    # Remove the key-value pair associated with the given key from the dictionary
    #!v
    del dictionary[key]
    #!^

def check_key_exists(dictionary, key):
    # Check if the given key exists in the dictionary
    #!v
    key_exists = key in dictionary
    #!^
    return key_exists
