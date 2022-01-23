# Задание 1
import time


class TrafficLight:
    __color = 'Red'

    def running(self):
        print(TrafficLight.__color)
        time.sleep(7)
        print('Yellow')
        time.sleep(2)
        print('Green')
        time.sleep(3)


a = TrafficLight()
a.running()


# Задание 2
class Road:
    def __init__(self, length, width):
        self._l = length
        self._w = width

    def mass_asfalt(self, mass_asf, tolshina):
        self.m = mass_asf
        self.t = tolshina
        return self._l * self._w * self.m * self.t


b = Road(20, 5000)
print(b.mass_asfalt(25, 5))


# Задание 3
class Worker:
    def __init__(self, name, surname, position, income):
        self.n = name
        self.s = surname
        self.p = position
        self._i = income



class Position(Worker):
    def get_full_name(self):
        print(f'Имя и фамилия работника {self.n} {self.s}')

    def get_total_income(self):
        print(f'Доход работника {sum(self._i.values())}')


n = input('Введите имя работника: ')
s = input('Введите фамилию работника: ')
p = input('Введите должность работника: ')
i = dict(zip(['wage', 'bonus'], map(int, input('Введите зп и премию работника через пробел: ').split(' '))))
r = Position(n, s, p, i)
r.get_full_name()
r.get_total_income()

# Задание 4
import random
class Car:
    def __init__(self, speed, color, name, is_police):
        self.s = speed
        self.c = color
        self.n = name
        self.i = is_police

    def show_speed(self):
        print(self.s)

    def go(self):
        if self.s > 0:
            print('Машина поехала')
        elif self.s < 0:
            print('Машина поехала назад')

    def stop(self):
        if self.s == 0:
            print('Машина стоит')

    def turn(self, direction):
        if direction.lower() == 'left':
            print('Машина повернула налево')
        elif direction.lower() == 'right':
            print('Машина повернула направо')


class TownCar(Car):
    def show_speed(self):
        print(self.s)
        if self.s > 60:
            print('Вы привысили скорость')


class SportCar(Car):
    def gonit(self):
        if self.s > 100:
            print('Пытается свалить от полиции')
        else:
            print('Практически не едем')

class WorkCar(Car):
    def show_speed(self):
        print(self.s)
        if self.s > 40:
            print('Снизьте скорость')

class PoliceCar(Car):
    def gibbd(self):
        if self.s > 100:
            print('Приследует нарушителя')
        else:
            print('Следит за скоростью')


random.choice(['left', 'right'])
autobus = TownCar(random.randrange(0, 100), 'red', 'Liaz', False)
tesla_sport = SportCar(random.randrange(0, 300), 'red', 'tesla', False)
gruzovink = WorkCar(random.randrange(0, 120), 'orange', 'Volvo', False)
police = PoliceCar(random.randrange(0, 200), 'blue', 'lada', True)
autobus.go()
autobus.stop()
autobus.turn(random.choice(['left', 'right']))
autobus.show_speed()
tesla_sport.go()
tesla_sport.stop()
tesla_sport.turn(random.choice(['left', 'right']))
tesla_sport.show_speed()
tesla_sport.gonit()
gruzovink.go()
gruzovink.stop()
gruzovink.turn(random.choice(['left', 'right']))
gruzovink.show_speed()
police.go()
police.stop()
police.turn(random.choice(['left', 'right']))
police.show_speed()
police.gibbd()

# Задание 5
class Stationery:
    def __init__(self, title):
        self.t = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Рисую ручкой')

class Pencil(Stationery):
    def draw(self):
        print('Время чертить карандашом')

class Handle(Stationery):
    def draw(self):
        print('Нарисуем что нибудь маркером?')

pen = Pen('EricCrauser')
pencil = Pencil('Конструктор')
handle = Handle('edding')
pen.draw()
pencil.draw()
handle.draw()



