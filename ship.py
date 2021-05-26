from field import Field


class Ship:
    start_coord: list
    direction: int
    ship_len: int
    hits: list

    # direstions: 1 - ↑, 2 - →, 3 - ↓, 4 - ←

    def __init__(self, start_coord: list, direction: int, ship_len: int, hits: list = None):
        self.start_coord = start_coord
        self.direction = direction
        self.ship_len = ship_len
        self.hits = hits

    def check_crossing(self, field: Field):
        if self.direction == 1:
            for i in range(self.start_coord[0], self.start_coord[0] + self.ship_len + 1):
                if field.field[i][self.start_coord[1]] != ' ':
                    return True
            return False
        if self.direction == 2:
            for i in range(self.start_coord[1], self.start_coord[1] + self.ship_len + 1):
                if field.field[self.start_coord[0]][i] != ' ':
                    return True
            return False
        if self.direction == 3:
            for i in range(self.start_coord[0], self.start_coord[0] - self.ship_len - 1):
                if field.field[i][self.start_coord[1]] != ' ':
                    return True
            return False
        if self.direction == 4:
            for i in range(self.start_coord[1], self.start_coord[1] - self.ship_len - 1):
                if field.field[self.start_coord[0]][i] != ' ':
                    return True
            return False

    def check_hits(self, hit_coord: list):
        if self.direction == 1:
            for i in range(self.start_coord[0], self.start_coord[0] + self.ship_len + 1):
                if [i, self.start_coord[1]] == hit_coord:
                    return True
            return False
        if self.direction == 2:
            for i in range(self.start_coord[1], self.start_coord[1] + self.ship_len + 1):
                if [self.start_coord[0], i] == hit_coord:
                    return True
            return False
        if self.direction == 3:
            for i in range(self.start_coord[0], self.start_coord[0] - self.ship_len - 1):
                if [i, self.start_coord[1]] == hit_coord:
                    return True
            return False
        if self.direction == 4:
            for i in range(self.start_coord[1], self.start_coord[1] - self.ship_len - 1):
                if [self.start_coord[0], i] == hit_coord:
                    return True
            return False

    def is_die(self):
        if self.hits is not None:
            if len(self.hits) == self.ship_len:
                return True
        return False