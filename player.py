from __future__ import annotations
from abc import abstractmethod
from math import radians
from field import Field
from ship import Ship
from random import randint

class Player(ABC):
    # количество возможных кораблей: количество палуб
    SHIPS_NUM = [0, 4, 3, 2, 1] 
    field: Field

    @abstractmethod
    def set_ships():
        pass


    @abstractmethod
    def move(opponent_field: Field):
        pass


    @abstractmethod
    def show_field(opponent_field: Field):
        pass


    def set_random(self):
        amount = 1
        for ship_size in range(len(Player.SHIPS_NUM), 0, -1):
            for j in range(amount):
                while True:
                start_coord_x = randint(1,10)
                start_coord_y = randint(1,10)
                ship_direction = randint(1,4)
                ship = Ship([start_coord_x, start_coord_y], ship_direction, ship_size, [])
                try:
                    self.field.add_ship(ship)
                except ValueError:
                    pass
                else: 
                    break
            amount += 1

