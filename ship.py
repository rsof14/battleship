from __future__ import annotations
import field as f


class Ship: # S: класс, в котором для каждого корабля определяются параметры (начальная координата, направление,
    # длина, массив ударов по этому кораблю), есть методы, определяющие, можно ли поставить корабль на поле,
    # попал ли выстрел по кораблю и затоплен ли корабль
    # O: не знаю, какие причины, кроме исправления ошибок
    start_coord: list
    direction: int
    ship_len: int
    hits: list
    DIRECTION_UP = 1
    DIRECTION_RIGHT = 2
    DIRECTION_DOWN = 3
    DIRECTION_LEFT = 4

    def __init__(self, start_coord: list, direction: int, ship_len: int):
        self.start_coord = start_coord
        self.direction = direction
        self.ship_len = ship_len
        self.hits = []

    def check_crossing(self, field: f.Field):
        # метод проверяет, пересекается ли корабль, который игрок хочет поставить, с лдругими уже стоящими на поле.
        # метод принимает поле, возвращает True, если есть пересечения, и корабль ставить нельзя. возвращает False,
        # если пересечений нет. Исключительные ситуации, если корабль, который игрок хочет поставить, выходит за
        # пределы поля
        if self.direction == self.DIRECTION_LEFT or self.direction == self.DIRECTION_RIGHT:
            if self.direction == self.DIRECTION_LEFT:
                step = -self.ship_len
                dir = -1
            else:
                step = self.ship_len
                dir = 1
            for i in range(self.start_coord[0], self.start_coord[0] + step, dir):
                if abs(i) >= 10 or abs(self.start_coord[1]) >= 10 or i < 0:
                    raise ValueError("Корабль выходит за пределы поля")
                if i - 1 < 0:
                    tk = 0
                else:
                    tk = i - 1
                if i + 2 > 9:
                    yk = 9
                else:
                    yk = i + 2
                if self.start_coord[1] - 1 < 0:
                    tj = 0
                else:
                    tj = self.start_coord[1] - 1
                if self.start_coord[1] + 2 > 9:
                    yj = 9
                else:
                    yj = self.start_coord[1] + 2
                for k in range(tk, yk):
                    for j in range(tj, yj):
                        if field.field[self.start_coord[1]][i] != ' ' or field.field[j][k] != ' ':
                            return True
            return False
        if self.direction == self.DIRECTION_UP or self.direction == self.DIRECTION_DOWN:
            if self.direction == self.DIRECTION_DOWN:
                step = -self.ship_len
                dir = -1
            else:
                step = self.ship_len
                dir = 1
            for i in range(self.start_coord[1], self.start_coord[1] + step, dir):
                if abs(i) >= 10 or abs(self.start_coord[1]) >= 10 or i < 0:
                    raise ValueError("Корабль выходит за пределы поля")
                if i - 1 < 0:
                    tk = 0
                else:
                    tk = i - 1
                if i + 2 > 9:
                    yk = 9
                else:
                    yk = i + 2
                if self.start_coord[0] - 1 < 0:
                    tj = 0
                else:
                    tj = self.start_coord[0] - 1
                if self.start_coord[0] + 2 > 9:
                    yj = 9
                else:
                    yj = self.start_coord[0] + 2
                for k in range(tk, yk):
                    for j in range(tj, yj):
                        if field.field[i][self.start_coord[0]] != ' ' or field.field[j][k] != ' ':
                            return True

            return False

    def check_hits(self, hit_coord: list):
        # метод проверяет, попал ли выстрел в корабль. метод принимает координаты выстрела, возвращает True,
        # если корабль ранен, False, если выстрел мимо корабля.
        if self.direction == self.DIRECTION_LEFT or self.direction == self.DIRECTION_RIGHT:
            if self.direction == self.DIRECTION_LEFT:
                step = -self.ship_len
                dir = -1
            else:
                step = self.ship_len
                dir = 1
            for i in range(self.start_coord[0], self.start_coord[0] + step, dir):
                if hit_coord == [i, self.start_coord[1]]:
                    self.hits.append(hit_coord)
                    return True
            return False
        if self.direction == self.DIRECTION_UP or self.direction == self.DIRECTION_DOWN:
            if self.direction == self.DIRECTION_DOWN:
                step = -self.ship_len
                dir = -1
            else:
                step = self.ship_len
                dir = 1
            for i in range(self.start_coord[1], self.start_coord[1] + step, dir):
                if hit_coord == [self.start_coord[0], i]:
                    self.hits.append(hit_coord)
                    return True
            return False

    def is_die(self):
        # метод проверяет, убит ли корабль. сравнивается длина корабля и количество попаданий по нему. Если корабль
        # убит, метод возвращает True, иначе - False
        if self.hits is not None:
            if len(self.hits) == self.ship_len:
                return True
        return False
