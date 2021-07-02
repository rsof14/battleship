from __future__ import annotations
import ship as sh


class Field:
    # S: класс для хранения поля и выполнения операций над ним: печать поля, переписывание координат, добавление
    # корабля, удар по координатам.
    ships: list[sh.Ship]
    hits_misses: list[list[str]]

    def __init__(self):
        self.ships = []
        self.hits_misses = []  # ? как хранить промахи, чтобы воссоздать их при печати и хранить
        self.field = [[' ' for i in range(10)] for i in range(10)]  # нужно ли это поле

    def print_my_field(self):
        # метод выводит поле игрока-человека
        # вынести принты в отдельный класс
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
        # метод выводит поле игрока-компьютера для игрока-человека
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
                    if self.field[i][j] != 'K':
                        print(self.field[i][j], end='')
                    else:
                        print(' ', end='')
            print()

    def set_coord(self, coord: str):
        # метод преобразует координаты из вида "буква-цифра" к виду "цифра-цифра". возвращает лист из двух координат
        # (только непонятно, какая - столбец, какая - строка). исключительные ситуации в случае, когда координаты
        # передаются в несоответсвующем формате
        words = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']
        if coord[0] not in words:
            raise ValueError("Несоответствующее значение")
        coord_y = words.index(coord[0])
        coord_x = int(coord[1:len(coord)])
        if not 1 <= coord_x <= 10:
            raise ValueError("Несоответствующее значение")
        return [coord_y, coord_x - 1]

    def add_ship(self, ship: sh.Ship):
        # метод отвечает за добавление корабля на поле. принимает корабль, проверяет, можно ли его поставить (это
        # лучше вынести в отдельный метод, как мне кажется), если можно, то корабль добавляется на поле,
        # иначе исключительная ситуация
        if ship.direction == ship.DIRECTION_LEFT or ship.direction == ship.DIRECTION_RIGHT:
            if ship.direction == ship.DIRECTION_LEFT:
                step = -ship.ship_len
                dir = -1
            else:
                step = ship.ship_len
                dir = 1
            for i in range(ship.start_coord[0], ship.start_coord[0] + step, dir):
                if abs(i) >= 10 or abs(ship.start_coord[1]) >= 10:
                    raise ValueError("Корабль выходит за пределы поля")
        if ship.direction == ship.DIRECTION_UP or ship.direction == ship.DIRECTION_DOWN:
            if ship.direction == ship.DIRECTION_DOWN:
                step = -ship.ship_len
                dir = -1
            else:
                step = ship.ship_len
                dir = 1
            for i in range(ship.start_coord[1], ship.start_coord[1] + step, dir):
                if abs(i) >= 10 or abs(ship.start_coord[1]) >= 10:
                    raise ValueError("Корабль выходит за пределы поля")
        if not ship.check_crossing(self):
            if ship.direction == ship.DIRECTION_LEFT or ship.direction == ship.DIRECTION_RIGHT:
                if ship.direction == ship.DIRECTION_LEFT:
                    step = -ship.ship_len
                    dir = -1
                else:
                    step = ship.ship_len
                    dir = 1
                for i in range(ship.start_coord[0], ship.start_coord[0] + step, dir):
                    if abs(i) >= 10 or abs(ship.start_coord[1]) >= 10:
                        raise ValueError("Корабль выходит за пределы поля")
                    self.field[ship.start_coord[1]][i] = 'K'
            if ship.direction == ship.DIRECTION_UP or ship.direction == ship.DIRECTION_DOWN:
                if ship.direction == ship.DIRECTION_DOWN:
                    step = -ship.ship_len
                    dir = -1
                else:
                    step = ship.ship_len
                    dir = 1
                for i in range(ship.start_coord[1], ship.start_coord[1] + step, dir):
                    if abs(i) >= 10 or abs(ship.start_coord[1]) >= 10:
                        raise ValueError("Корабль выходит за пределы поля")
                    self.field[i][ship.start_coord[0]] = 'K'
            self.ships.append(ship)
        else:
            raise ValueError("Корабли не могут пересекаться")

    def to_hit(self, coord: list):
        # метод отвечает за удар по данным координатам (координаты удара передаются). метод меняет значение клетки
        # поля в зависимости от попадания/непопадания
        flag = False
        for ship in self.ships:
            # if not ship.check_hits(coord):
            #     self.field[coord[1]][coord[0]] = '.'
            # else:
            #     self.field[coord[1]][coord[0]] = 'o'
            if ship.check_hits(coord):
                self.field[coord[1]][coord[0]] = 'o'
                flag = True
            if ship.is_died():
                if ship.direction == ship.DIRECTION_LEFT or ship.direction == ship.DIRECTION_RIGHT:
                    if ship.direction == ship.DIRECTION_LEFT:
                        step = -ship.ship_len
                        dir = -1
                    else:
                        step = ship.ship_len
                        dir = 1
                    for i in range(ship.start_coord[0], ship.start_coord[0] + step, dir):
                        if i - 1 < 0:
                            tk = 0
                        else:
                            tk = i - 1
                        if i + 2 > 9:
                            yk = 9
                        else:
                            yk = i + 2
                        if ship.start_coord[1] - 1 < 0:
                            tj = 0
                        else:
                            tj = ship.start_coord[1] - 1
                        if ship.start_coord[1] + 2 > 9:
                            yj = 9
                        else:
                            yj = ship.start_coord[1] + 2
                        for k in range(tk, yk):
                            for j in range(tj, yj):
                                self.field[j][k] = '.'
                        self.field[ship.start_coord[1]][i] = 'x'
                if ship.direction == ship.DIRECTION_UP or ship.direction == ship.DIRECTION_DOWN:
                    if ship.direction == ship.DIRECTION_DOWN:
                        step = -ship.ship_len
                        dir = -1
                    else:
                        step = ship.ship_len
                        dir = 1
                    for i in range(ship.start_coord[1], ship.start_coord[1] + step, dir):
                        if i - 1 < 0:
                            tk = 0
                        else:
                            tk = i - 1
                        if i + 2 > 9:
                            yk = 9
                        else:
                            yk = i + 2
                        if ship.start_coord[0] - 1 < 0:
                            tj = 0
                        else:
                            tj = ship.start_coord[0] - 1
                        if ship.start_coord[0] + 2 > 9:
                            yj = 9
                        else:
                            yj = ship.start_coord[0] + 2
                        for k in range(tk, yk):
                            for j in range(tj, yj):
                                self.field[k][j] = '.'
                        self.field[i][ship.start_coord[0]] = 'x'
                self.ships.remove(ship)
                break
        if not flag:
            self.field[coord[1]][coord[0]] = '.'
