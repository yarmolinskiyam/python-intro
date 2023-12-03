def declaration():
    # Объяви переменную x, равную 10
    #!v

    #!^
    return x

def multi_declaration():
    # На одной строчке объяви переменные a, b, c и d, равные 10, 20, 30 и 40 соответственно
    #!v

    #!^
    return (a, b, c, d)

def bools():
    # Объяви переменную TRUEE равную истине (True)
    #!v

    #!^
    return TRUEE

def types():
    # Объяви три переменных: var_int, var_float и var_bool так, чтобы они были типов int, float и bool соответственно
    #!v
    var_int = x
    var_float = x
    var_bool = x
    #!^
    return (type(var_int), type(var_float), type(var_bool))

def strings():
    # Создай строку hello_world с текстом "Hello world!"
    #!v

    #!^
    return hello_world

def string_concat():
    hello = "Hello"
    space = " "
    world = "world!"
    # Используя уже объявленные строки и операцию конкатенации
    #  создай строку hello_world с текстом "Hello world!"
    #!v

    #!^
    return hello_world

def string_convertion():
    a = 123
    # Преобразуй переменную a в строку a_str с соответствующим значением с помощью str()
    #!v
    
    #!^
    return a_str

def calculator():
    a, b = 10, 3
    # Используя переменные a и b вычисли сумму, разность, произведение,
    #  частное, частное (при целочисленном делении),
    #  остаток от деления, степень и сохрани их в соответствующие переменные
    #!v
    sum = x # сумма
    dif = x # разность
    mul = x # произведение
    divf = x # частное (вещественное деление)
    divi = x # частное (целочисленное деление)
    rem = x # остаток от деления
    pow = x # степень
    #!^
    return (sum, dif, mul, divf, divi, rem, pow)

