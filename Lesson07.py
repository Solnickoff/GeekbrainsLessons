# Задание 1
import random


class Matrix():
    def __init__(self, spisok):
        self.s = spisok

    def __str__(self):
        a = ''
        for i in self.s:
            a += ' '.join(str(k) for k in i) + '\n'
        return a

    def __add__(self, other):
        a = []
        for i in range(len(self.s)):
            b = []
            for k in range(len(self.s[i])):
                b.append(self.s[i][k] + other.s[i][k])
            a.append(b)
        return Matrix(a)


def shmatrix(a, b):
    z = []
    for i in range(a):
        x = []
        for k in range(b):
            x.append(random.randrange(-100, 100))
        z.append(x)
    return z


a = Matrix(shmatrix(int(input('Введите кол-во строк: ')), int(input('Введите кол-во столбцов: '))))
b = Matrix(shmatrix(int(input('Введите кол-во строк: ')), int(input('Введите кол-во столбцов: '))))
print(a)
print(b)
print(a + b)

# Задание 2
from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def consumption_coat(self):
        pass

    @abstractmethod
    def consumption_costume(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.v = size

    @property
    def consumption_coat(self):
        return round(self.v / 6.5 + 0.5, 1)

    def consumption_costume(self):
        pass


class Costume(Clothes):
    def __init__(self, height):
        self.h = height

    def consumption_coat(self):
        pass

    @property
    def consumption_costume(self):
        return round(self.h * 2 + 0.3, 1)


jacket = Costume(int(input('Введите размер костюма: ')))
coat = Coat(int(input('Введите размер пальто: ')))
print(f'Расход ткани на костюм: {jacket.consumption_costume}')
print(f'Расход ткани на пальто: {coat.consumption_coat}')
print(f'Общий расход ткани: {jacket.consumption_costume + coat.consumption_coat}')


# Задание 3
class Cell:
    def __init__(self, number_cells):
        self.n = number_cells

    def __add__(self, other):
        return Cell(self.n + other.n)

    def __sub__(self, other):
        return Cell(self.n - other.n)

    def __mul__(self, other):
        return Cell(round(self.n * other.n))

    def __truediv__(self, other):
        return Cell(round(self.n / other.n))

    def __str__(self):
        return f'Клетка {self.n}'

    def make_ord(self, number_cell):
        row = []
        while self.n >= number_cell:
            row.append('*' * abs(self.n - number_cell - self.n))
            self.n -= number_cell
            if self.n < number_cell:
                row.append('*' * self.n)
        return '\n'.join(row)


c = Cell(int(input('Введите количество клеток: ')))
print(Cell(10) * Cell(3.489))
print(c.make_ord(int(input('Введите количество клеток в ряду: '))))

