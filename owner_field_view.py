from field import Field


class OwnerFieldView:
    my_field: Field
    RAW0 = [' ', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']

    def __init__(self, my_field: Field):
        self.my_field = my_field

    def make_field(self):  # сделать классы для полей и из них печатать
        my_field = [[' ' for i in range(0, 11)] for i in range(0, 11)]
        my_field[0] = self.RAW0
        for i in range(1, 11):
            my_field[i][0] = i
        for ship in self.my_field.ships:
            for ship_coord in ship.all_cd():
                my_field[ship_coord.row][ship_coord.col] = 'K'
        for hits_misses in self.my_field.hits_misses:
            if self.my_field.hits_misses[hits_misses] is True:
                my_field[hits_misses.row][hits_misses.col] = 'o'
            else:
                my_field[hits_misses.row][hits_misses.col] = '.'
        for ship_coord in self.my_field.died_ships:
            my_field[ship_coord.row][ship_coord.col] = 'x'
        return my_field

    def print_field(self):
        my_field = self.make_field()
        for i in range(11):
            for j in range(11):
                print(my_field[i][j], end='')
            print()
