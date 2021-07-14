import field as fd
import ship as sh
import point as point


class Print:
    RAW0 = [' ', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']

    def __init__(self, my_field: fd.Field, opponent_field: fd.Field):
        self.my_field = my_field
        self.opponent_field = opponent_field

    def make_my_field(self): # сделать классы для полей и из них печатать
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
        opponent_field = [[' ' for i in range(1, 11)] for i in range(1, 11)]
        opponent_field[0] = self.RAW0
        for i in range(1, 11):
            opponent_field[i][0] = i
        for hits_misses in self.opponent_field.hits_misses:
            if hits_misses is True:
                opponent_field[hits_misses.row][hits_misses.col] = 'o'
            else:
                opponent_field[hits_misses.row][hits_misses.col] = '.'
        for ship_coord in self.opponent_field.died_ships:
            opponent_field[ship_coord.row][ship_coord.col] = 'x'
        return opponent_field

    def print_my_field(self):
        my_field = self.make_my_field()
        for i in range(11):
            for j in range(11):
                print(my_field[i][j], end='')
            print()

    def print_opponent_field(self):
        opponent_field = self.make_opponent_field()
        for i in range(11):
            for j in range(11):
                print(opponent_field[i][j], end='')
            print()

