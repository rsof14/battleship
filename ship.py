from __future__ import annotations
import field as f
import rectangle as r
import point 


class Ship:  # S: класс, в котором для каждого корабля определяются параметры (начальная координата, направление,
    # длина, массив ударов по этому кораблю), есть методы, определяющие, можно ли поставить корабль на поле,
    # попал ли выстрел по кораблю и затоплен ли корабль
    # O: не знаю, какие причины, кроме исправления ошибок
    start_coord: point.Point
    direction: int
    ship_len: int
    hits: set
    DIRECTION_RIGHT = 1
    DIRECTION_DOWN = 2

    def __init__(self, start_coord: point.Point, direction: int, ship_len: int):
        self.start_coord = start_coord
        self.direction = direction
        self.ship_len = ship_len
        self.hits = set()
        self.small_rectangle = r.Rectangle(self.start_coord, self.direction, self.ship_len)
        self.big_rectangle = r.Rectangle(self.start_coord, self.direction, self.ship_len).big_rectangle()
        self.all_coords = [self.start_coord]
        # теперь прямоугольник изначально маленький

    def all_cd(self):
        if self.direction == self.DIRECTION_RIGHT:
            for i in range(1, self.ship_len):
                self.all_coords.append(point.Point(self.start_coord.row, self.start_coord.col + i))  # сработает или нет?
        if self.direction == self.DIRECTION_DOWN:
            for i in range(1, self.ship_len):
                self.all_coords.append(point.Point(self.start_coord.row + i, self.start_coord.col))
        return self.all_coords

    def out_of_field(self):
        for i in range(4):
            if self.small_rectangle.small_rectangle[i] < 0 or self.small_rectangle.small_rectangle[i] > 9:
                return False
        return True

    def check_crossing(self, other_ship: Ship):
        # !!!поменять вызов этой функции (в классе field должен быть цикл по всем
        # кораблям, который сравнивает два корабля)
        # метод проверяет, пересекается ли корабль, который игрок хочет поставить, с лдругими уже стоящими на поле.
        # метод принимает поле, возвращает True, если есть пересечения, и корабль ставить нельзя. возвращает False,
        # если пересечений нет. Исключительные ситуации, если корабль, который игрок хочет поставить, выходит за
        # пределы поля.
        # вынести проверку на выход за поле
        # создать поле с прямоугольной областью вокруг корабля, либо класс прямоугольник для геом. операций!!!!
        # проверять пересечение двух кораблей, т.е. пересечение двух прямоугольников
        if self.out_of_field():
            return self.small_rectangle.check_crossing(other_ship.big_rectangle)
        else:
            raise ValueError("Корабль выходит за пределы поля")

    def add_hits(self, hit_coord: point.Point):
        if self.check_hits(hit_coord):
            self.hits.add(hit_coord)

    def check_hits(self, hit_coord: point.Point):
        # метод проверяет, попал ли выстрел в корабль. метод принимает координаты выстрела, возвращает True,
        # если корабль ранен, False, если выстрел мимо корабля. добавить в прямоугольник метод, проверяющий,
        # попала ли точка в прямоугольник создать два прямоугольника для одного корабля: большой и маленький сделать
        # в чек хитс только проверку попадания, пополнять список попаданий в другом методе, который вызывает чек хитс
        # для проверки. проверять в хитс, чтобы все элементы были разными
        return self.small_rectangle.hit(hit_coord)

    def is_died(self):
        # метод проверяет, убит ли корабль. сравнивается длина корабля и количество попаданий по нему. Если корабль
        # убит, метод возвращает True, иначе - False
        if self.hits is not None:   # относится ли None к сету?
            if len(self.hits) == self.ship_len:
                return True
        return False
