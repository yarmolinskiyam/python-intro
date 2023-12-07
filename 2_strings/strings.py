def create_string():
    # Create a string with the value "Hello, world!"
    #!v
    my_string = "Hello, world!"
    #!^
    return my_string

def access_char(string, index):
    # Return the character at the given index of the string
    #!v
    character = string[index]
    #!^
    return character

def slice_string(string, start, end):
    # Return a sliced portion of the string from start to end
    #!v
    sliced_string = string[start:end]
    #!^
    return sliced_string

def concatenate_strings(string1, string2):
    # Concatenate two strings
    #!v
    concatenated_string = string1 + string2
    #!^
    return concatenated_string

def uppercase_string(string):
    # Convert the string to uppercase
    #!v
    uppercase_str = string.upper()
    #!^
    return uppercase_str

def lowercase_string(string):
    # Convert the string to lowercase
    #!v
    lowercase_str = string.lower()
    #!^
    return lowercase_str
