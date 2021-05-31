from ship import Ship


class Field:
    ships: list[Ship]
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
                    print(' ')
                if i == -1 and j != -1:
                    print(words[j])
                if i != -1 and j == -1:
                    print(i + 1)
                if i != -1 and j != -1:
                    print(self.field[i][j])

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

    def add_ship(self, ship: Ship):
        if ship.check_crossing(self.field) is False:
            if ship.direction == ship.DIRECTION_LEFT or ship.direction == ship.DIRECTION_RIGHT:
                if ship.direction == ship.DIRECTION_LEFT:
                    step = -1 * ship.ship_len - 1
                if ship.direction == ship.DIRECTION_RIGHT:
                    step = ship.ship_len + 1
                for i in range(ship.start_coord[0], ship.start_coord[0] + step):
                    self.field[i][ship.start_coord[1]] = '□'
            if ship.direction == ship.DIRECTION_UP or ship.direction == ship.DIRECTION_DOWN:
                if ship.direction == ship.DIRECTION_DOWN:
                    step = -1 * ship.ship_len - 1
                if ship.direction == ship.DIRECTION_UP:
                    step = ship.ship_len + 1
                for i in range(ship.start_coord[1], ship.start_coord[1] + step):
                    self.field[ship.start_coord[0]][i] = '□'
            self.ships.append(ship)

    def to_hit(self, coord: list):
        if Ship.check_hits(coord) is False:
            self.field[coord[0]][coord[1]] = '.'
        else:
            self.field[coord[0]][coord[1]] = 'o'
        for ship in self.ships:
            if ship.is_die() is True:
                if ship.direction == ship.DIRECTION_LEFT or ship.direction == ship.DIRECTION_RIGHT:
                    if ship.direction == ship.DIRECTION_LEFT:
                        step = -1 * ship.ship_len - 1
                    if ship.direction == ship.DIRECTION_RIGHT:
                        step = ship.ship_len + 1
                    for i in range(ship.start_coord[0], ship.start_coord[0] + step):
                        for k in range(i - 1, i + 2):
                            for j in range(ship.start_coord[0] - 1, ship.start_coord[0] + 2):
                                self.field[k][j] = '.'
                        self.field[i][ship.start_coord[1]] = 'x'
                if ship.direction == ship.DIRECTION_UP or ship.direction == ship.DIRECTION_DOWN:
                    if ship.direction == ship.DIRECTION_DOWN:
                        step = -1 * ship.ship_len - 1
                    if ship.direction == ship.DIRECTION_UP:
                        step = ship.ship_len + 1
                    for i in range(ship.start_coord[1], ship.start_coord[1] + step):
                        for k in range(ship.start_coord[1] - 1, ship.start_coord[1] + 2):
                            for j in range(i - 1, i + 2):
                                self.field[k][j] = '.'
                        self.field[0][i] = 'x'
                self.ships.remove(ship)
                break
