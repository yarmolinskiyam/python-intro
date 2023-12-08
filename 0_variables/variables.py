def declaration():
    # Объяви переменную x, равную 10
    #!v
    x = 10
    #!^
    return x

def multi_declaration():
    # На одной строчке объяви переменные a, b, c и d, равные 10, 20, 30 и 40 соответственно
    #!v
    a,b,c,d = 10,20,30,40
    #!^
    return (a, b, c, d)

def bools():
    # Объяви переменную TRUEE равную истине (True)
    #!v
    TRUEE = True
    #!^
    return TRUEE

def types():
    # Объяви три переменных: var_int, var_float и var_bool так, чтобы они были типов int, float и bool соответственно
    #!v
    var_int = 10
    var_float = 10.0
    var_bool = True
    #!^
    return (type(var_int), type(var_float), type(var_bool))

def strings():
    # Создай строку hello_world с текстом "Hello world!"
    #!v
    hello_world = "Hello world!"
    #!^
    return hello_world

def string_concat():
    hello = "Hello"
    space = " "
    world = "world!"
    # Используя уже объявленные строки и операцию конкатенации
    #  создай строку hello_world с текстом "Hello world!"
    #!v
    hello_world = "Hello world!"
    #!^
    return hello_world

def string_convertion():
    a = 123
    # Преобразуй переменную a в строку a_str с соответствующим значением с помощью str()
    #!v
    a_str = str(a)
    #!^
    return a_str

def calculator():
    a, b = 10, 3
    # Используя переменные a и b вычисли сумму, разность, произведение,
    #  частное, частное (при целочисленном делении),
    #  остаток от деления, степень и сохрани их в соответствующие переменные
    #!v
    sum = a+b # сумма
    dif = a-b # разность
    mul = a*b # произведение
    divf = a/b # частное (вещественное деление)
    divi = a//b # частное (целочисленное деление)
    rem = a%b # остаток от деления
    pow = a**b # степень
    #!^
    return (sum, dif, mul, divf, divi, rem, pow)

