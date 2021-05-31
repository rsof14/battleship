from random import randint
from player import Player
from field import Field

class ComputerPlayer(Player):
    def set_ships(self):
        self.set_random()
    

    def move(self):
        marked_cell_x = randint(1, 10)
        marked_cell_y = randint(1,10)
        marked_cell = [marked_cell_x, marked_cell_y]
        if marked_cell not in self.field.hits_misses:
            if self.HumanPlayer.field[marked_cell_x][marked_cell_y] == ' ':
                self.HumanPlayer.field[marked_cell_x][marked_cell_y] = '.'
            else:
                self.HumanPlayer.field[marked_cell_x][marked_cell_y] = 'x'
                # обратиться к кораблю ПРОТИВНИКА и изменить его hits


    def show_field(self, opponent_field: Field):
        pass