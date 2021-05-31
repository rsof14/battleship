from random import randint
from player import Player
from field import Field

class ComputerPlayer(Player):
    def set_ships(self):
        self.set_random()
    

    def move(self, opponent_field: Field):
        marked_cell_x = randint(1, 10)
        marked_cell_y = randint(1,10)
        opponent_field.to_hit([marked_cell_x, marked_cell_y])


    def show_field(self, opponent_field: Field):
        pass