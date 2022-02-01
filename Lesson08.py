# Задание 1
class Date:
    @classmethod
    def numbers(cls, date):
        months = dict(
            zip(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                 'November', 'December'], [i for i in range(1, 13)]))
        date = date.split('-')
        date[1] = months[date[1]]
        date = list(map(int, date))
        return date

    @staticmethod
    def validate_numbers(date):
        if 1 <= Date.numbers(date)[0] <= 31:
            print('Число месяца указано верно')
        else:
            print('Неправильно указано число месяца')
        if 1 <= Date.numbers(date)[1] <= 12:
            print('Месяц указан верно')
        else:
            print('Месяц указан неверно')


print(Date.numbers('10-January-2012'))
print(Date.validate_numbers('10-January-2012'))


# Задание 2
class Errors(Exception):
    def __init__(self):
        self.t = 'Вы попытались поделить на ноль'

    def __str__(self):
        return self.t


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

try:
    if b == 0:
        raise Errors()
    c = a / b
except ValueError:
    print('Вы ввели не числа')
except Errors as err:
    print(err)
else:
    print(f'{c}')


# Задание 3
class ErrorsInput(Exception):
    def __init__(self, list_users):
        self.l = 'В вашем тексте есть другой символ вместо цифр'
        self.u = list_users

    def list_of_numbers(self):
        list_num = [i for i in self.u if i in '1234567890']
        return ', '.join(list_num)

    def __str__(self):
        return self.l + '\n' + f'Вот список цифр без букв и символов {self.list_of_numbers()}'


while True:
    try:
        a = input('Введите список чисел: ')
        if a.lower() == 'stop':
            break
        for i in a:
            if i not in '1234567890':
                raise ErrorsInput(a)
    except ErrorsInput as err:
        print(err)
    else:
        print(ErrorsInput(a))


# Задание 4, 5, 6
class Store:
    def __init__(self, amount_equipment, max_amount):
        self.e = amount_equipment
        self.m = max_amount

    def __iadd__(self, other):
        if self.e < self.m:
            self.e += other.a
        else:
            print('Склад полон')
        return self

    def __sub__(self, other):
        if self.e > 0:
            self.e -= other.a
        else:
            print('Склад пуст')
        return self

    def __str__(self):
        return f'Техники на складе, шт.: {self.e}'


class OfficeEquipment:
    def __init__(self):
        self.color = ['color', 'b/w']


class Printer(OfficeEquipment):
    def __init__(self, mark_of_printer, amount):
        super().__init__()
        try:
            self.a = amount
            for i in self.a:
                if i not in '0123456789':
                    raise Validate_Number
                else:
                    self.a = int(amount)
        except Validate_Number as err:
            print(err)
        self.t = mark_of_printer

    def list_printer(self):
        list_p = {self.t: [self.color, self.a]}
        return list_p


class Scaner(OfficeEquipment):
    def __init__(self, mark_of_scaner, amount):
        super().__init__()
        try:
            self.a = amount
            for i in self.a:
                if i not in '0123456789':
                    raise Validate_Number
                else:
                    self.a = int(amount)
        except Validate_Number as err:
            print(err)
        self.t = mark_of_scaner

    def list_scaner(self):
        list_s = {self.t: [self.color, self.a]}
        return list_s


class Xerox(OfficeEquipment):
    def __init__(self, mark_of_xerox, amount):
        super().__init__()
        try:
            self.a = amount
            for i in self.a:
                if i not in '0123456789':
                    raise Validate_Number
                else:
                    self.a = int(amount)
        except Validate_Number as err:
            print(err)
        self.t = mark_of_xerox

    def list_xerox(self):
        list_x = {self.t: [self.color, self.a]}
        return list_x


class Validate_Number(Exception):
    def __init__(self):
        self.t = 'Вы ввели неправильно количество'

    def __str__(self):
        return f'{self.t}'


def add_equipment(store, equpmint):
    store += equpmint
    print(store)


store = Store(0, int(input('Введите максимальную вместительность склада, шт: ')))
printers = Printer(input('Введите название марку принтера: '), input('Введите количество принтеров: '))
add_equipment(store, printers)
scaners = Scaner(input('Введите название марку сканера: '), input('Введите количество сканера: '))
add_equipment(store, scaners)
xerox = Xerox(input('Введите название марку ксерокса: '), input('Введите количество ксерокса: '))
add_equipment(store, xerox)


def get_equepmint(store, a):
    store -= a
    print(store)


get_equepmint(store, int(input('Сколько вы хотите забрать шт. техники: ')))

# Задание 7
class ComplexNumbers:
    def __init__(self, complex_number):
        self.comnu = complex_number
        self.comnu = self.comnu.split(' ')

    def __add__(self, other):
        if (int(self.comnu[2][:-1]) + int(other.comnu[2][:-1])) < 0:
            return str((int(self.comnu[0]) + int(other.comnu[0]))) + '-' + str((int(self.comnu[2][:-1]) + int(other.comnu[2][:-1]))) + 'i'
        else:
            return str((int(self.comnu[0]) + int(other.comnu[0]))) + '+' + str((int(self.comnu[2][:-1]) + int(other.comnu[2][:-1]))) + 'i'

    def __mul__(self, other):
        if int(self.comnu[2][:-1]) * int(other.comnu[0]) + int(self.comnu[0])* int(other.comnu[2][:-1]) < 0:
            return str(int(self.comnu[0]) * int(other.comnu[0]) - int(self.comnu[2][:-1]) * int(other.comnu[2][:-1])) + '-' + str(int(self.comnu[2][:-1]) * int(other.comnu[0]) + int(self.comnu[0])* int(other.comnu[2][:-1])) + 'i'
        else:
            return str(int(self.comnu[0]) * int(other.comnu[0]) - int(self.comnu[2][:-1]) * int(other.comnu[2][:-1])) + '-' + str(int(self.comnu[2][:-1]) * int(other.comnu[0]) + int(self.comnu[0])* int(other.comnu[2][:-1])) + 'i'


a = ComplexNumbers(input('Введите комплексное число через вида "a +/- bi": '))
b = ComplexNumbers(input('Введите комплексное число через вида "a +/- bi": '))

print(a + b)
print(a * b)

