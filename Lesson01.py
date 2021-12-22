# Задание 1
a = 10
b = 30
c = int(input('Введите число: '))
d = int(input('Введите число: '))
print(c)
print(d)
# Задание 2
seconds = int(input('Введите количество секунд: '))
hour = seconds//3600
seconds %= 3600
minute = seconds//60
seconds %= 60
if seconds > 10:
    sec = str(seconds)
else:
    sec = '0' + str(seconds)
if minute > 10:
    minute = str(minute)
else:
    minute = '0' + str(minute)
if hour > 10:
    hour = str(hour)
else:
    hour = '0' + str(hour)
print(f'{hour}:{minute}:{sec}')

# Задание 3
user_number = int(input('Введите число: '))
suma = user_number + int(str(user_number) * 2) + int(str(user_number) * 3)
print(suma)

# Задание 4
user_number1 = int(input('Введите число: '))
max_number = user_number1 % 10
while user_number1 > 0:
    last_number = user_number1 % 10
    user_number1 //= 10
    if max_number < last_number:
        max_number = last_number
print(f'Максимальная цифра = {max_number}')

# Задание 5
viruchka = int(input('Введите выручку: '))
izderjki = int(input('Введите издержки: '))
workers = int(input('Введите количество сотрудников: '))
if viruchka > izderjki:
    print(f'Прибыль составила {viruchka - izderjki} рублей, рентабельность {(viruchka - izderjki)/viruchka * 100}%')
    print(f'Прибыль на сотрудника составила {(viruchka - izderjki) / workers} рублей')
elif viruchka < izderjki:
    print(f'Фирма работает в убыток {izderjki - viruchka} рублей')
else:
    print('Вы работаете в ноль')

# Задание 6
a = int(input('Введите результат спортсмена в первый день, км: '))
b = int(input('Введите результат спортсмена, которого хотите достич, км: '))
day = 1
while a < b:
    a += a * 0.1
    day += 1
    print(f'{day}-й день: {a}')
print(f'На {day}-й день спортсмен достиг результата - не менее {b} км.')
