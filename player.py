from __future__ import annotations
from abc import ABC, abstractmethod
from field import Field
from ship import Ship
from random import randint


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

    def set_random(self):
        for ship_size in range(len(Player.SHIPS_NUM), 0, -1):
            for j in range(Player.SHIPS_NUM[ship_size]):
                while True:
                    start_coord_x = randint(1, 10)
                    start_coord_y = randint(1, 10)
                    ship_direction = randint(1, 4)
                    ship = Ship([start_coord_x, start_coord_y], ship_direction, ship_size)
                    try:
                        self.field.add_ship(ship)
                    except ValueError:
                        pass
                    else:
                        break
