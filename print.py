import field as fd
import ship as sh
import point as point


class Print:
    RAW0 = [' ', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']

    def __init__(self, my_field: fd.Field, opponent_field: fd.Field):
        self.my_field = my_field
        self.opponent_field = opponent_field

    def make_my_field(self):
        my_field = [[' ' for i in range(1, 11)] for i in range(1, 11)]
        my_field[0] = self.RAW0
        for i in range(1, 11):
            my_field[i][0] = i
        for ship in self.my_field.ships:
            for ship_coord in ship.all_coords:
                my_field[ship_coord.row][ship_coord.col] = 'K'
        for hits_misses in self.my_field.hits_misses:
            if hits_misses is True:
                my_field[hits_misses.row][hits_misses.col] = 'o'
            else:
                my_field[hits_misses.row][hits_misses.col] = '.'
        for ship_coord in self.my_field.died_ships:
            my_field[ship_coord.row][ship_coord.col] = 'x'
        return my_field

    def make_opponent_field(self):
        pass

    def print_my_field(self):
        my_field = self.make_my_field()
        for i in range(11):
            for j in range(11):
                print(my_field[i][j], end='')
            print()

    def print_opponent_field(self):
        pass
