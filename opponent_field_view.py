from field import Field


class OpponentFieldView:
    RAW0 = [' ', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']

    def __init__(self, opponent_field: Field):
        self.opponent_field = opponent_field

    def make_field(self):
        opponent_field = [[' ' for i in range(0, 11)] for i in range(0, 11)]
        opponent_field[0] = self.RAW0
        for i in range(1, 11):
            opponent_field[i][0] = i
        for hits_misses in self.opponent_field.hits_misses:
            if self.opponent_field.hits_misses[hits_misses] is True:
                opponent_field[hits_misses.row][hits_misses.col] = 'o'
            else:
                opponent_field[hits_misses.row][hits_misses.col] = '.'
        for ship_coord in self.opponent_field.died_ships:
            opponent_field[ship_coord.row][ship_coord.col] = 'x'
        return opponent_field

    def print_field(self):
        opponent_field = self.make_field()
        for i in range(11):
            for j in range(11):
                print(opponent_field[i][j], end='')
            print()

