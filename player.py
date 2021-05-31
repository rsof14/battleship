from __future__ import annotations
from abc import abstractmethod
from math import radians
from field import Field
from ship import Ship
from random import randint

class Player(ABC):
    # количество возможных кораблей: количество палуб
    SHIPS_NUM = {4: 1, 3: 2, 2: 3, 1: 4} 
    field: Field

    @abstractmethod
    def set_ships():
        pass


    @abstractmethod
    def move():
        pass


    @abstractmethod
    def show_field(opponent_field: Field):
        pass


    def set_random():
        amount = 1
        for i in range(len(self.SHIPS_NUM)):
            for j in range(amount):
                ship_size = self.SHIPS_NUM[i + 1]
                start_coord_x = randint(1,10)
                start_coord_y = randint(1,10)
                start_coord = [start_coord_x, start_coord_y]
                ship_direction = radint(1, 4)
                ship = Ship(start_coord, ship_direction, ship_size, [])
                self.field.add_ship(ship)
            amount += 1

