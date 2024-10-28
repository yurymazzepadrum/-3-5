#----------------------------------------------------------DZ Рекурсия
def get_multiplied_digits(number):
    str_number = str(number) # Создайте переменную str_number и запишите строковое представление(str) числа number в неё.
    first = int(str_number[0]) # создайте переменную first и запишите в неё первый символ из str_number в числовом представлении(int).
    if len(str_number) > 1:
        return  first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first






result = get_multiplied_digits(40203)
print(result)
