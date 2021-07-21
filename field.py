from __future__ import annotations
import ship as sh
import point


class Field:
    # S: класс для хранения поля и выполнения операций над ним: печать поля, переписывание координат, добавление
    # корабля, удар по координатам.
    ships: list[sh.Ship]
    hits_misses: dict
    died_ships: list # координаты всех клеток, где были корабли, которые сейчас убиты

    def __init__(self):
        self.ships = []
        self.hits_misses = {}  # ? как хранить промахи, чтобы воссоздать их при печати и хранить
        self.died_ships = []
        self.around_died_ships = []
        self.field = [[' ' for i in range(10)] for i in range(10)]  # нужно ли это поле

    def set_coord(self, coord: str):
        # метод преобразует координаты из вида "буква-цифра" к виду "цифра-цифра". возвращает лист из двух координат
        # (только непонятно, какая - столбец, какая - строка). исключительные ситуации в случае, когда координаты
        # передаются в несоответсвующем формате
        # хранить координаты в датаклассе Point
        start_coord = point.Point.from_string(coord)
        return start_coord


    def add_ship(self, ship: sh.Ship):
        # метод отвечает за добавление корабля на поле. принимает корабль, проверяет, можно ли его поставить (это
        # лучше вынести в отдельный метод, как мне кажется), если можно, то корабль добавляется на поле,
        # иначе исключительная ситуация
        # придумать, как добавлять корабль в виде символа на поле
        if not ship.out_of_field():
            raise ValueError("Корабль выходит за пределы поля")
        for other_ship in self.ships:
            if ship.check_crossing(other_ship):
                raise ValueError("Корабли не могут пересекаться")
        self.ships.append(ship)

    def to_hit(self, coord: point.Point):
        # метод отвечает за удар по данным координатам (координаты удара передаются). метод меняет значение клетки
        # поля в зависимости от попадания/непопадания
        flag = False
        for ship in self.ships:
            if ship.check_hits(coord):
                ship.add_hits(coord)
                self.hits_misses[coord] = True
                flag = True
            if ship.is_died():
                for around_coord in ship.small_rectangle.big_rectangle_all_cd():
                    self.around_died_ships.append(around_coord)
                    # self.hits_misses[around_coord] = False
                for ship_coord in ship.all_cd():
                    self.died_ships.append(ship_coord)

                    self.around_died_ships.remove(ship_coord)
                    deleted = self.hits_misses.pop(ship_coord, None)

                    #self.died_ships.append(self.hits_misses.pop(ship_coord))
                self.ships.remove(ship)
                break
        if not flag:
            self.hits_misses[coord] = False
