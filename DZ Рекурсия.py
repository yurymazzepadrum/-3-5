#----------------------------------------------------------DZ Рекурсия
# Напишите функцию get_multiplied_digits и параметр number в ней.

def get_multiplied_digits(number):
# Создайте переменную str_number и запишите строковое представление(str) числа number в неё.
    str_number = '40203'
# Основной задачей будет отделение первой цифры в числе: создайте переменную first и запишите в неё первый символ из str_number в числовом представлении(int)
    first = 4
# Возвращайте значение first * get_multiplied_digits(int(str_number[1:]))
    return first * get_multiplied_digits(int(str_number[1:]))
    if str_number == 0:
        return first





result = get_multiplied_digits(40203)
print(result)