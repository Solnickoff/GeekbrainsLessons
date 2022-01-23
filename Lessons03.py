# Задание 1
def delenie(a, b):
    while a.isalpha() or b.isalpha():
        print('Введите число, а не символ')
        a, b = input('Введите число: '), input('Введите число: ')
    while a.isdigit() and b.isdigit():
        try:
            res = int(a) / int(b)
            print('Результат деления: ', res)
            print('Хотите остановиться, то введите любой символ вместо числа')
        except ZeroDivisionError:
            print('Делить на ноль нельзя')
        a, b = input('Введите число: '), input('Введите число: ')


x, y = input('Введите число: '), input('Введите число: ')

delenie(x, y)


# Задание 2
def data_from_user(name, surname, years, city, email, telephone):
    print(f'{surname} {name} {years} года рождения, проживающего в городе {city}, email: {email}, телефон: {telephone}')


a, b = input('Введите свое имя: '), input('Введите свою фамилию: ')
c, d = input('Введите свой год рождения: '), input('Введите свой город проживания: ')
e, f = input('Введите своq email: '), input('Введите свой номер телефона: ')

data_from_user(a, b, c, d, e, f)


# Задание 3
def my_func(a, b, c):
    list_chisel = [int(a), int(b), int(c)]
    max1 = max(list_chisel)
    list_chisel.remove(max1)
    max2 = max(list_chisel)
    print(f'Сумма двух максимальных значений из 3 чисел равна {max1 + max2}')


a, b, c = input('Введите первое число: '), input('Введите второе число: '), input('Введите третие число: ')
while a.isalpha() or b.isalpha() or c.isalpha():
    print('Введите числа, а не символы')
    a, b, c = input('Введите первое число: '), input('Введите второе число: '), input('Введите третие число: ')

my_func(a, b, c)


# Задание 4
def func_stepen(x, y):
    for i in range(abs(y)):
        x *= x
    print(f'Результат возведения числа в отрицательной степени равен {1 / x}')


num1, num2 = input('Ввеедите число, которое хотите возвести в степень: '), input('Укажите степень: ')
while num1.isalpha() or num2.isalpha() or int(num2) > 0:
    print('Вы ввели не те значения, введите числа, а степень в отрицательном значении')
    num1, num2 = input('Ввеедите число, которое хотите возвести в степень: '), input('Укажите степень: ')

func_stepen(int(num1), int(num2))


# Задание 5
def suma_chisel():
    sum_numbers = 0
    while True:
        numbers = input('Введите числа через пробел, если хотите остановиться введите любой символ: ').split()
        for i in range(len(numbers)):
            try:
                numbers[i] = int(numbers[i])
                sum_numbers += numbers[i]
            except ValueError:
                print(sum_numbers)
                return
        print(sum_numbers)


suma_chisel()


# Задание 6
def int_func(text):
    new_text = list(map(lambda x: x.capitalize(), text))
    print(' '.join(new_text))


int_func(input('Введите латинские слова через пробел: ').split(' '))
