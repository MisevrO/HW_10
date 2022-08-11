# Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель",
# наслідувані від "Транспортний засіб".
# Наповніть класи атрибутами на свій розсуд.
# Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель".

class Vehicle:
    """
    Class atеribute
    """
    fly = 'sky'
    drive = 'road'
    swim = 'sea'
    def __init__(self, fly, drive,swim ):
        self.fly = fly
        self.drive = drive
        self.swim = swim

class Car(Vehicle):
    """
    The ancestral class is indicated in parentheses
    """
    wheel = 4
    steer = 'black'

    def super_drive(self):
        return super().drive

class Plane(Vehicle):
    wings = ''
    pilot = ''

    def super_fly(self):
        return super().fly

class Ship(Vehicle):
    anchor = 1
    arrt = 2

    def __init__(self, attr):
        self.anchor = attr

    def thing(self):
        print(f'attr is {self.anchor}')

    def super_swim(self):
        return super().swim