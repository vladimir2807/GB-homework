def div(*args):
    try:
        arg1 = int(input("Делимое "))
        arg2 = int(input("Делитель "))
        res = arg1 / arg2
    except ValueError:
        return "Ошибка вывода"
    except ZeroDivisionError:
        return "Нельзя делить на ноль, введите другое значение!"
    return res

print(f"Результат  {div()}")
#------------------------------------------------2---------------------------------------------------
def person(name, lastname, year_of_birth, city, email, phone):
    return print(f'Имя: {name} Фамилия: {lastname} Год рождения: {year_of_birth}'
                 f'Город проживания: {city} Email: {email} Телефон: {phone}')


person(
    name=input('Имя: '),
    lastname=input('Фамилия: '),
    year_of_birth=input('Год Рождения: '),
    city=input('Город проживания: '),
    email=input('email: '),
    phone=input('phone: '),
)
#------------------------------------------------3---------------------------------------------------
def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(f'Результат - {my_func(int(input("Введите первое значение ")), int(input("Введите второй значение ")), int(input("Введите третье значение ")))}')
#------------------------------------------------4---------------------------------------------------
def my_func(x, y):
    return x ** y
#------------------------------------------------5---------------------------------------------------
def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите число или Q для выхода ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Сумма на данный момент: {sum_res}')
    print(f'Финальный результат: {sum_res}')


my_sum()

#------------------------------------------------6---------------------------------------------------

def int_func (*args):
    word = input("Введите слово: ")
    print(word.title())
    return
int_func()