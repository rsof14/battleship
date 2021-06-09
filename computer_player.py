from random import randint
from player import Player
from field import Field


class ComputerPlayer(Player):
    NAME = "Компьютер"  # нужно, чтобы проще вывести победителя в Game.move

    def set_ships(self):
        self.set_random()

    def move(self, opponent_field: Field):
        # Я переделяю под while, просто пока ещё мозг тупит + времени нет
        already_hit = []
        marked_cell_x = randint(0, 9)
        marked_cell_y = randint(0, 9)
        point = str(marked_cell_x) + str(marked_cell_y)
        if point not in already_hit:
            opponent_field.to_hit([marked_cell_x, marked_cell_y])
            already_hit.append(str(str(marked_cell_x) + str(marked_cell_y)))

    def show_field(self, opponent_field: Field):
        pass
