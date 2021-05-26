from ship import Ship


class Field:
    ships: list[Ship]
    hits_misses: list[list[str]]

    def __init__(self, ships: list[Ship], hits_misses: list[list[str]]):
        self.ships = ships
        self.hits_misses = hits_misses
        self.field = [[' '] * 10] * 10

    def print_field(self):
        pass

    def add_ship(self, ship: Ship):
        pass

    def to_hit(self, coord: list):
        pass
