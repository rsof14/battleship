from __future__ import annotations
from abc import ABC, abstractmethod
from field import Field
from ship import Ship
from random import randint
from point import Point

"""
Абстрактный класс Игрок. Нужен для определения поведения классов Человек-Игрок и Игрок-Компьютер.
"""

class Player(ABC):
    SHIPS_NUM = [0, 4, 3, 2, 1]
    NAME: str  # нужно, чтобы проще вывести победителя в Game.move
    field: Field

    def __init__(self):
        self.field = Field()

    @abstractmethod
    def set_ships(self):
        pass

    @abstractmethod
    def move(self, opponent_field: Field):
        pass

    @abstractmethod
    def show_field(self, opponent_field: Field):
        pass

    """
    Этот метод случайным образом производит расстановку кораблей на поле.
    Если добавить корабль в поле можно, исключительных ситуаций не возникает.
    Иначе возникает ValueError.
    """
    def set_randomly(self):
        for ship_size in range(len(Player.SHIPS_NUM) - 1, 0, -1):
            for j in range(Player.SHIPS_NUM[ship_size]):
                while True:
                    row = randint(1, 10)
                    col = randint(1, 10)
                    ship_direction = randint(1, 2) # осталось два направления - вправо и вниз, вправо - 1, вниз - 2
                    ship = Ship(Point(row, col), ship_direction, ship_size)
                    try:
                        self.field.add_ship(ship)
                    except ValueError as e:
                        #print(e)
                        pass
                    else:
                        break
