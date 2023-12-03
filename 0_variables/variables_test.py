import variables

def test_variables():
    assert variables.declaration() == 10
    assert variables.multi_declaration() == (10, 20, 30, 40)
    assert variables.bools() == True
    assert variables.types() == (int, float, bool)
    assert variables.strings() == "Hello world!"
    assert variables.string_concat() == "Hello world!"
    assert variables.string_convertion() == "123"
    assert variables.calculator() == (13, 7, 30, 10/3, 3, 1, 1000)