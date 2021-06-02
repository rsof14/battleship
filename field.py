from __future__ import annotations
import ship as sh


class Field:
    ships: list[sh.Ship]
    hits_misses: list[list[str]]

    def __init__(self):
        self.ships = []
        self.hits_misses = []
        self.field = [[' '] * 10] * 10

    def print_my_field(self):
        words = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']
        for i in range(-1, 10):
            for j in range(-1, 10):
                if i == -1 and j == -1:
                    print(' ', end='')
                if i == -1 and j != -1:
                    print(words[j], end='')
                if i != -1 and j == -1:
                    print(i + 1, end='')
                if i != -1 and j != -1:
                    print(self.field[i][j], end='')
            print()

    def print_opponent_field(self):
        words = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']
        for i in range(-1, 10):
            for j in range(-1, 10):
                if i == -1 and j == -1:
                    print(' ')
                if i == -1 and j != -1:
                    print(words[j])
                if i != -1 and j == -1:
                    print(i + 1)
                if i != -1 and j != -1:
                    if self.field[i][j] != '□':
                        print(self.field[i][j])
                    else:
                        print(' ')

    def set_coord(self, coord: str):
        words = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']
        if coord not in words:
            raise ValueError("Несоответствующее значение")
        coord0 = words.index(coord[0])
        coord1 = int(coord[1:len(coord)])
        if not 0 <= coord1 <= 10:
            raise ValueError("Несоответствующее значение")
        return [coord0, coord1]

    def add_ship(self, ship: sh.Ship):
        if not ship.check_crossing(self):
            if ship.direction == ship.DIRECTION_LEFT or ship.direction == ship.DIRECTION_RIGHT:
                if ship.direction == ship.DIRECTION_LEFT:
                    step = -1 * ship.ship_len - 1
                else:
                    step = ship.ship_len + 1
                for i in range(ship.start_coord[0], ship.start_coord[0] + step):
                    if abs(i) > 10 or abs(ship.start_coord[1]) > 10:
                        raise ValueError("Корабль выходит за пределы поля")
                    self.field[i][ship.start_coord[1]] = '□'
            if ship.direction == ship.DIRECTION_UP or ship.direction == ship.DIRECTION_DOWN:
                if ship.direction == ship.DIRECTION_DOWN:
                    step = -1 * ship.ship_len - 1
                else:
                    step = ship.ship_len + 1
                for i in range(ship.start_coord[1], ship.start_coord[1] + step):
                    if abs(i) > 10 or abs(ship.start_coord[1]) > 10:
                        raise ValueError("Корабль выходит за пределы поля")
                    self.field[ship.start_coord[0]][i] = '□'
            self.ships.append(ship)
        else:
            raise ValueError("Корабли не могут пересекаться")

    def to_hit(self, coord: list):
        for ship in self.ships:
            if not ship.check_hits(coord):
                self.field[coord[0]][coord[1]] = '.'
            else:
                self.field[coord[0]][coord[1]] = 'o'
            if ship.is_die():
                if ship.direction == ship.DIRECTION_LEFT or ship.direction == ship.DIRECTION_RIGHT:
                    if ship.direction == ship.DIRECTION_LEFT:
                        step = -1 * ship.ship_len - 1
                    else:
                        step = ship.ship_len + 1
                    for i in range(ship.start_coord[0], ship.start_coord[0] + step):
                        for k in range(i - 1, i + 2):
                            for j in range(ship.start_coord[0] - 1, ship.start_coord[0] + 2):
                                self.field[k][j] = '.'
                        self.field[i][ship.start_coord[1]] = 'x'
                if ship.direction == ship.DIRECTION_UP or ship.direction == ship.DIRECTION_DOWN:
                    if ship.direction == ship.DIRECTION_DOWN:
                        step = -1 * ship.ship_len - 1
                    else:
                        step = ship.ship_len + 1
                    for i in range(ship.start_coord[1], ship.start_coord[1] + step):
                        for k in range(ship.start_coord[1] - 1, ship.start_coord[1] + 2):
                            for j in range(i - 1, i + 2):
                                self.field[k][j] = '.'
                        self.field[0][i] = 'x'
                self.ships.remove(ship)
                break
