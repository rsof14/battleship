from field import Field


class Ship:
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

    def check_crossing(self, field: Field):
        if self.direction == self.DIRECTION_LEFT or self.direction == self.DIRECTION_RIGHT:
            if self.direction == self.DIRECTION_LEFT:
                step = -1 * self.ship_len - 1
            if self.direction == self.DIRECTION_RIGHT:
                step = self.ship_len + 1
            for i in range(self.start_coord[0], self.start_coord[0] + step):
                if field.field[i][self.start_coord[1]] != ' ':
                    return True
            return False
        if self.direction == self.DIRECTION_UP or self.direction == self.DIRECTION_DOWN:
            if self.direction == self.DIRECTION_DOWN:
                step = -1 * self.ship_len - 1
            if self.direction == self.DIRECTION_UP:
                step = self.ship_len + 1
            for i in range(self.start_coord[1], self.start_coord[1] + step):
                if field.field[self.start_coord[0]][i] != ' ':
                    return True
            return False

    def check_hits(self, hit_coord: list):
        if self.direction == self.DIRECTION_LEFT or self.direction == self.DIRECTION_RIGHT:
            if self.direction == self.DIRECTION_LEFT:
                step = -1 * self.ship_len - 1
            if self.direction == self.DIRECTION_RIGHT:
                step = self.ship_len + 1
            for i in range(self.start_coord[0], self.start_coord[0] + step):
                if hit_coord == [i, self.start_coord[1]]:
                    self.hits.append(hit_coord)
                    return True
            return False
        if self.direction == self.DIRECTION_UP or self.direction == self.DIRECTION_DOWN:
            if self.direction == self.DIRECTION_DOWN:
                step = -1 * self.ship_len - 1
            if self.direction == self.DIRECTION_UP:
                step = self.ship_len + 1
            for i in range(self.start_coord[1], self.start_coord[1] + step):
                if hit_coord == [self.start_coord[0], i]:
                    self.hits.append(hit_coord)
                    return True
            return False

    def is_die(self):
        if self.hits is not None:
            if len(self.hits) == self.ship_len:
                return True
        return False
