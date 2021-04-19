#-------------------------------------------------1------------------------------------------------------------
my_list = [99, None, {5, 3, 1, 0, 2, 4}, -31, (1, 2, 3, 4), 'False', True, 9.5]
def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return
my_type(my_list)

#-------------------------------------------------2------------------------------------------------------------
el_count = int(input("Введите значение:"))
my_list = []
i = 0
el = 0
while i < el_count:
    my_list.append(input("Введите следующее значение:"))
    i += 1

    for elem in range(int(len(my_list) / 2)):
        my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
        el += 2
    print(my_list)

#-------------------------------------------------3------------------------------------------------------------
seasons_list = ["Зима", "Весна", "Лето", "Осень"]
seasons_dict = {1:"Зима", 2:"Весна", 3:"Лето", 4:"Осень"}

month = int(input("Введите месяц по номеру "))
if month <= 12 and month >= 1:
    month_dict = {1:"Январь",
               2:"Февраль",
               3:"Март",
               4:"Апрель",
               5:"Май",
               6:"Июнь",
               7:"Июль",
               8:"Август",
               9:"Сентябрь",
               10:"Октябрь",
               11:"Ноябрь",
               12:"Декабрь"}
    month_list = list(month_dict.values())
    for i, el in enumerate(month_list):
        if i == month-1:
            print(f"Месяц {month_list[i]}")
            break
    print(f"Месяц {month_dict[month]}")
if month ==1 or month == 12 or month == 2:
        print(seasons_dict.get(1))
        print(seasons_list[0])

elif month == 3 or month == 4 or month ==5:
    print(seasons_dict.get(2))
    print(seasons_list[1])

elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])

elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
        print("Такого месяца не существует")
#-------------------------------------------------4------------------------------------------------------------
my_str = input("Введите данные сроки")
my_word = []
num = 1
for el in range(my_str.count(' ') + 1):
    my_word = my_str.split()
    if len(str(my_word)) <= 10:
        print(f" {num} {my_word [el]}")
        num += 1
    else:
        print(f" {num} {my_word [el] [0:10]}")
        num += 1

#-------------------------------------------------5------------------------------------------------------------
my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
digit = int(input("Введите ваше значение от 1 до 10 (11 - для выхода) "))
while digit != 11:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
    print(f"Текущий список - {my_list}")
    digit = int(input("Введите ваше значение от 1 до 10 (11 - для выхода)"))