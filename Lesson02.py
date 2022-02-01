# Задание 1
Spisok = [1, 2345.123, 'Privet', [1, 23, 0], (1, 2, 3), {'1': 1, '2': 2}, {1, 2, 3, 4}]
for i in Spisok:
    print(type(i))

# Задание 2
spisok = input('Введите список через пробел: ').split()
for i in range(0, len(spisok) - 1, 2):
    spisok[i], spisok[i + 1] = spisok[i + 1], spisok[i]
print(spisok)

# Задание 3
user = int(input('Введите месяц в виде числа: '))
month = ['Winter', 'Spring', 'Summer', 'Autumn']
month1 = {(12, 1, 2): 'Winter', (3, 4, 5): 'Spring', (6, 7, 8): 'Summer', (9, 10, 11): 'Autumn'}
if 1 <= user <= 2 or user == 12:
    print(month[0])
elif 3 <= user <= 5:
    print(month[1])
elif 6 <= user <= 8:
    print(month[2])
else:
    print(month[3])
for k in month1:
    if user in k:
        print(month1[k])
        break

# Задание 4
user = input('Введите слова через пробел: ').split()
for e, i in enumerate(user):
    if len(i) > 10:
        print(e, i[:10])
    else:
        print(e, i)

# Задание 5
my_list = [7, 5, 3, 3, 2]
user = 0
while user != ' ':
    try:
        user = int(input('Введите рейтинг: '))
    except:
        print(my_list)
        break
    my_list.append(user)
    my_list.sort()
    my_list.reverse()
    print(my_list)

# или
my_list = [7, 5, 3, 3, 2]
user = 0
while user != '':
    try:
        user = int(input('Введите рейтинг: '))
    except:
        print(my_list)
        break
    if user > my_list[0]:
        my_list.insert(0, user)
    elif user in my_list:
        my_list.insert(my_list.index(user) + my_list.count(user), user)
    elif user not in my_list:
        if user < my_list[-1]:
            my_list.append(user)
        else:
            for i in range(1, len(my_list)):
                if user > my_list[i]:
                    my_list.insert(my_list.index(my_list[i]), user)
                    break
    print(my_list)

# Задание 6
goods = []
keys = ['название', 'цена', 'количество', 'ед']
while True:
    user = input('Введите через пробел название товара, цену, количество, единицы измерения(выход = Enter): ')
    if user == '':
        break
    user = user.split()
    for i in range(len(user)):
        if user[i].isdigit():
            user[i] = int(user[i])
    good = dict(zip(keys, user))
    goods.append(good)

kol = (i for i in range(1, len(goods) + 1))
tovars = [*zip(kol, goods)]
print(tovars)
naz = []
cena = []
kolich = []
edin = []
for i in goods:
    naz.append(i['название'])
    cena.append(i['цена'])
    kolich.append(i['количество'])
    edin.append(i['ед'])
    edin = set(edin)
    edin = list(edin)
all_tov = [naz, cena, kolich, edin]
goods2 = dict(zip(keys, all_tov))
print(goods2)
