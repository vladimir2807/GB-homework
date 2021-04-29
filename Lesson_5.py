my_f = open('test.txt', 'w', encoding='utf-8')
line = input('Введите текст \n')
while line:
    my_f.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

my_f.close()
my_f = open('test.txt', 'r')
content = my_f.readlines()
print(content)
my_f.close()
#--------------------------------------------------2----------------------------------------------------------
my_file = open('file1.txt', 'r', encoding="utf-8")
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file = open('file1.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
my_file = open('file1.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Количество символов {i + 1} - ой строки {len(content[i])}')
my_file = open('file1.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()
#--------------------------------------------------3----------------------------------------------------------
with open('text_3.txt', 'r', encoding="utf-8") as my_file:
    sal = []
    poor = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
           poor.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(float, sal)) / len(sal)}')
#--------------------------------------------------4----------------------------------------------------------
rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('text_4.txt', 'r', encoding='utf-8') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('text_44.txt', 'w', encoding='utf-8') as file_obj_2:
    file_obj_2.writelines(new_file)
#--------------------------------------------------5----------------------------------------------------------
def summary():
    try:
        with open('file_5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summary()
#--------------------------------------------------6----------------------------------------------------------
def count_subjects():
    try:
        mydict = {}
        with open("text_6.txt", encoding='utf-8') as fobj:
            for line in fobj:
                name, stats = line.split(':')
                name_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split()))
                mydict[name] = name_sum
            print(f"{mydict}")
    except FileNotFoundError:
        return 'Файл не найден.'

count_subjects()
#--------------------------------------------------7----------------------------------------------------------
    import json

    def get_statistics():
        try:
            with open('text_7.txt', 'r+', encoding='utf-8') as file:
                statistics = []
                profit = {}
                average_profit = {}
                av = 0
                prof = 0
                i = 3
                for line in file:
                    name, firm, earning, damage = line.split()
                    total = int(earning) - int(damage)
                    if total >= 0:
                        prof = prof + total
                    else:
                        i -= 1
                    profit[name] = total
                statistics.append(profit)
                if i != 0:
                    (av) = prof / i
                    average_profit['average_profit'] = round(av)
                    statistics.append(average_profit)
                else:
                    print('Все компании работают в убыток')
                print(statistics)
            with open('file.json', 'a+', encoding='utf-8') as json_file:
                json.dump(statistics, json_file)
        except FileNotFoundError:
            return 'Файл не найден.'

    get_statistics()