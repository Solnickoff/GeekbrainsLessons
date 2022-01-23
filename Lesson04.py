# Задание 1
from sys import argv

try:
    name_script, virabotka_vchas, stavka_v_chas, premia = argv
    print(f'Зарплата работника {int(virabotka_vchas) * int(stavka_v_chas) + int(premia)}')
except ValueError:
    print('Вы ввели мало/много значений, введите заново')

# Задание 2
import random

spisok_chisel = [i + random.randrange(0, 500) for i in range(random.randint(0, 20))]
new_spisok_chisel = [spisok_chisel[i] for i in range(1, len(spisok_chisel)) if spisok_chisel[i] > spisok_chisel[i - 1]]
print(f'Изначальный список {spisok_chisel}')
print(f'Обработанный список {new_spisok_chisel}')

# Задание 3
print([i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0])

# Задание 4
spisok = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([i for i in spisok if spisok.count(i) == 1])

# Задание 5
from functools import reduce


def proizvedenie(x, y):
    return x * y


print(reduce(proizvedenie, [i for i in range(100, 1001, 2)]))

# Задание 6
from sys import argv
from itertools import cycle, count

name_script, chislo, spisok_iter = argv
c = 0
for i in count(int(chislo)):
    if c < 10:
        print(i)
    else:
        break
    c += 1
c = 0
for i in cycle(spisok_iter):
    if c < len(spisok_iter) * 2:
        print(i)
    else:
        break
    c += 1


# Задание 7
from math import factorial
def fact(n):
    for el in range(1, n):
        yield factorial(el)


for el in fact(int(input()) + 1):
    print(el)
