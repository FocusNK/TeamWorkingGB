import main
from fractions import Fraction
# fraction фукнция для работы с рациональными числами. Fration(верхнее значение, нижнее)
# (real_number).as_integer_ratio() преобразование в рациональное число

a_string = main.get_value() # получение строки из терминала ссылаясь на файл main.py
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

# while True:
#     op = input('Operation: ')
#     if op not in func.keys():
#         break
#     print('{} {} {} = {}'.format(a, op, b, func[op](int(a), int(b))))










import main
from fractions import Fraction
# fraction фукнция для работы с рациональными числами. Fration(верхнее значение, нижнее)
# (real_number).as_integer_ratio() преобразование в рациональное число

a_string = main.get_value() # получение строки из терминала ссылаясь на файл
for character in '-+*/,%': #исключение из строки
    a_string = a_string.replace(character, '') #при нахождении знака, замени на null
print(a_string)
int_lst = [int(x) for x in a_string] # записываем полученную строку как целоечисленное 
print(int_lst) # [4, 3, 2, 3]

# with open('input.txt') as f:
#     a, b = f.read().split(maxsplit=2)
#     print("Read from file: {}, {}".format(a, b))
 













# str_lst = []
# for new_str in res_str:
#     str_lst.append(res_str)

# print("Строка после удаления всех символов: " + res_str)
# str_lst = str.replace('+', '0')
# print("Строка после удаления всех символов: " + str_lst)
# str_lst = res_str
# int_lst = [int(x) for x in str_lst]
# print(int_lst)
# print(sum(int_lst))

# from fractions import Fraction

# y = Fraction.from_float(2.25) # y = 9/4
# print(y)
# x = Fraction(11, 4)
# print(x)
# summa = 0


# def RationalPlus(a,b):
#     return Summa = Fraction(a,b) + Fraction(m,n)
    

# RationalPlus(5,6,3,2)
# print(Summa)


# a = Fraction(5, 6) + Fraction(3, 2) # a =   7/3
# b = a - Fraction(3, 5) # b = 26/15
# c = b * Fraction(101, 202) # c = 13/15
# d = c / b # d = 1/2
# e = d % a # e = 1/2
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# (real_number).as_integer_ratio()
# преобразование в дробное число
# a = (3.5).as_integer_ratio() # a = (7, 2)
# b = (11.7).as_integer_ratio() # b = (3293257227514675, 281474976710656)

# преобразование в тип Fraction
# a = 8.5
# c = Fraction(*a.as_integer_ratio()) # c =   17/2

# func = {'*': lambda x, y: x * y, '+': lambda x, y: x + y,
#         '-': lambda x, y: x - y, '/': lambda x, y: x / y}



# str = (input("Введите вещественное число: "))  
# res_str = str.replace(',', '0') 
# print("Строка после удаления всех символов ",": " + res_str)
# str_lst = res_str
# int_lst = [int(x) for x in str_lst]
# print(int_lst)
# print(sum(int_lst))


# a_string = [4/3+3/3] 
# a_string = (input("Введите вещественное число: ")) # ручной ввод.
# with open(main.py) as a_string:
#     a_string.read().split(maxsplit=2)
#     print("Read from file: {}, {}".format(a, b))