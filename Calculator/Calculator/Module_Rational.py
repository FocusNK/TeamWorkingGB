import main
from fractions import Fraction
# fraction фукнция для работы с рациональными числами. Fration(верхнее значение, нижнее)
# (real_number).as_integer_ratio() преобразование в рациональное число



a_string = main.get_value() # получение строки из терминала запуская файл main.py
for num in '-+*/,%': #исключение из строки
    a_string = a_string.replace(num, '') #при нахождении знака, замени на null
print(a_string)
int_lst = [int(x) for x in a_string] # записываем полученную строку как целоечисленное 
print(int_lst) # [4, 3, 2, 3]
a_funtions = main.get_value_func()
if a_funtions == "+":
    x = Fraction(int_lst[0], int_lst[1])
    y = Fraction(int_lst[2], int_lst[3])
    b = x + y 
    print (b)
elif a_funtions == "-":
    x = Fraction(int_lst[0], int_lst[1])
    y = Fraction(int_lst[2], int_lst[3])
    b = x - y 
    print (b)
elif a_funtions == "*":
    x = Fraction(int_lst[0], int_lst[1])
    y = Fraction(int_lst[2], int_lst[3])
    b = x * y 
    print (b)
elif a_funtions == "/":
    x = Fraction(int_lst[0], int_lst[1])
    y = Fraction(int_lst[2], int_lst[3])
    b = x / y 
    print (b)