from __future__ import annotations
import ship as sh
import point


class Rectangle:
    def __init__(self, start_coord: point.Point, direction, ship_len):
        self.start_coord = start_coord
        self.direction = direction  # оставлю направления вправо и вниз
        self.ship_len = ship_len
        if self.direction == sh.Ship.DIRECTION_RIGHT:
            self.small_rectangle = [self.start_coord.row, self.start_coord.col, self.start_coord.row,
                                    self.start_coord.col + self.ship_len]
        else:
            self.small_rectangle = [self.start_coord.row, self.start_coord.col, self.start_coord.row + self.ship_len,
                                    self.start_coord.col]

    def big_rectangle(self):
        if self.direction == sh.Ship.DIRECTION_RIGHT:
            big_rectangle = [self.start_coord.row - 1, self.start_coord.col - 1, self.start_coord.row + 1,
                             self.start_coord.col + self.ship_len]
        else:
            big_rectangle = [self.start_coord.row - 1, self.start_coord.col - 1, self.start_coord.row + self.ship_len,
                             self.start_coord.col + 1]
        for i in range(4):
            if big_rectangle[i] < 1:
                big_rectangle[i] += 1
            if big_rectangle[i] > 10:
                big_rectangle[i] -= 1
        return big_rectangle

    def big_rectangle_all_cd(self):
        br = self.big_rectangle()
        all_cd = []
        for row in range(br[0], br[2] + 1):
            for col in range(br[1], br[3] + 1):
                all_cd.append(point.Point(row, col))
        return all_cd

    def check_crossing(self,
                       other_ship_big_rectangle: Rectangle):  # проверить еще раз после того, как координаты стали point
        a_x = other_ship_big_rectangle[0]
        a_y = other_ship_big_rectangle[1]
        a_x1 = other_ship_big_rectangle[2]
        a_y1 = other_ship_big_rectangle[3]
        b_x = self.small_rectangle[0]
        b_y = self.small_rectangle[1]
        b_x1 = self.small_rectangle[2]
        b_y1 = self.small_rectangle[3]
        return (b_x <= a_x <= b_x1 or a_x <= b_x <= a_x1) and (b_y <= a_y <= b_y1 or a_y <= b_y <= a_y1)

    def hit(self, hit_coord: point.Point):
        return self.small_rectangle[0] <= hit_coord.row <= self.small_rectangle[2] and self.small_rectangle[
            1] <= hit_coord.col <= self.small_rectangle[3]
