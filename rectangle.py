from ship import Ship


class Rectangle:
    def __init__(self, start_coord, direction, ship_len):
        self.start_coord = start_coord
        self.direction = direction  # оставлю направления вправо и вниз
        self.ship_len = ship_len
        self.coord_y = self.start_coord[0]
        self.coord_x = self.start_coord[1]

    def small_rectangle(self):
        if self.direction == Ship.DIRECTION_RIGHT:
            return [self.start_coord[0], self.start_coord[1], self.start_coord[0] + self.ship_len, self.start_coord[1]]
        else:
            return [self.start_coord[0], self.start_coord[1], self.start_coord[0], self.start_coord[1] + self.ship_len]

    def big_rectangle(self):
        if self.direction == Ship.DIRECTION_RIGHT:
            big_rectangle = [self.coord_y - 1, self.coord_x - 1, self.coord_y + self.ship_len + 1, self.coord_x + 1]
        else:
            big_rectangle = [self.coord_y - 1, self.coord_x - 1, self.coord_y + 1, self.coord_x + self.ship_len + 1]
        for i in range (4):
            if big_rectangle[i] < 0:
                big_rectangle += 1
            if big_rectangle[i] > 9:
                big_rectangle -= 1
        return big_rectangle

    def check_crossing(self, other_ship: Ship):
        a_x = self.big_rectangle()[0]
        a_y = self.big_rectangle()[1]
        a_x1 = self.big_rectangle()[2]
        a_y1 = self.big_rectangle()[3]
        b_x = other_ship.small_rectangle[0]
        b_y = other_ship.small_rectangle[1]
        b_x1 = other_ship.small_rectangle[2]
        b_y1 = other_ship.small_rectangle[3]
        return (b_x < a_x < b_x1 or a_x < b_x < a_x1) and (b_y < a_y < b_y1 or a_y < b_y < a_y1)

