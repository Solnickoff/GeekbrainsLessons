# Задание 1
def UserData():
    file_name = input('Введите название файла: ')
    with open(f'{file_name}.txt', 'w') as f:
        text_user = input('Введите данные в файл(для выхода нажмите дважды Enter): ')
        print(text_user, end='\n', file=f)
        while text_user != '':
            text_user = input()
            print(text_user, end='\n', file=f)


UserData()

# Задание 2
def podschet():
    with open('zad2.txt', 'r') as g:
        leters = g.readlines()
        print('Количество строк в файле ', len(leters))
        count = 0
        g.seek(0)
        for i in g:
            count += len(i.split(' '))
        print(f'Количество слов в файле {count}')


podschet()

# Задание 3
def Sotrudniki():
    with open('Zad3.txt', 'r', encoding='UTF-8') as f:
        avg_zp = 0
        kol = 0
        sotr = []
        for i in f:
            kol += 1
            z = i.split(' ')
            if float(z[1]) < 20000:
                sotr.append(z[0])
            avg_zp += float(z[1])
        sotr = ', '.join(sotr)
        print(f'Список всех сотрудников с зарплатой меньше 20 тыс.: {sotr}')
        print(f'Средняя зарплата {round(avg_zp/kol, 2)}')


Sotrudniki()

# Задание 4
def smena_lang():
    with open('zad4.txt', 'r', encoding='UTF-8') as z:
        perevod = ['Один', 'Два', 'Три', 'Четыре']
        k= 0
        for i in z:
            a = i.split(' ')
            a[0] = perevod[k]
            k += 1
            with open('newfile.txt', 'a', encoding='UTF-8') as j:
                j.write(' '.join(a))


smena_lang()

# Задание 5
def creatsumma():
    from random import randint, randrange
    with open('newfile2.txt', 'w+', encoding='UTF-8') as k:
        for i in range(randrange(5, 20)):
            a = randint(0, 100)
            k.write(f'{str(a)} ')
        k.seek(0)
        print(f'Сумма всех чисел в файлу равна {sum(map(int, k.readline().split()))}')


creatsumma()

# Задание 6
def formdict():
    import re
    with open('zad6.txt', 'r', encoding='UTF-8') as k:
        keys = []
        value = []
        for i in k:
            keys.append(i.split(' ')[0][:-1])
            value.append(sum(map(int, re.findall(r'\d+', i))))
        print(dict(zip(keys, value)))


formdict()

# задание 7
def firms():
    import json
    import re
    with open('Zad7.txt', 'r', encoding='UTF-8') as k:
        keys_prib = []
        values_prib = []
        keys_ub = []
        values_ub = []
        for i in k:
            b = i.split(' ')[0]
            a = list(map(int, re.findall(r'\d+', i[7:])))
            if a[0] - a[1] < 0:
                keys_ub.append(b)
                values_ub.append(a[0] - a[1])
            else:
                keys_prib.append(b)
                values_prib.append(a[0] - a[1])
        avr_prof = sum(values_prib) / len(values_prib)
        firms_prib = [dict(zip(keys_prib, values_prib)), {"average_profit": avr_prof}]
        firms_ub = [dict(zip(keys_ub, values_ub))]
        print(f'Список фирм с прибылью и средняя прибыль {firms_prib}')
        print(f'Список фирм с убылью {firms_ub}')
        with open('new_json.json', 'w') as j:
            json.dump(firms_prib, j)
            print()
            json.dump(firms_ub, j)


firms()
