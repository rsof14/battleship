from random import randint
from field import Field
from ship import Ship
from computer_player import ComputerPlayer
from human_player import HumanPLayer
from player import Player


class Game:
    players: list[Player]

    def __init__(self):
        self.players = [HumanPLayer, ComputerPlayer]

    def set_ships(self):
        if int(input('нажмите 1, чтобы расставить корабли самостоятельно, нажмите 2, '
                     'чтобы расставить корабли в случайном порядке')) == 1:
            self.players[0].set_ships()
        else:
            self.players[0].set_random()
        self.players[1].set_random()

    def move(self):
        first_player = randint(1, 2)
        if first_player == 1:
            print("Случайным образом выбрано: вы ходите первыми")
            turn = 0
        else:
            print("Случайным образом выбрано: компьютер ходит первым")
            turn = -1
        while len(self.players[0].field.ships) != 0 and len(self.players[1].field.ships) != 0:
            self.players[turn % 2].move()
            self.players[turn % 2].show_field()
            turn += 1
            if len(self.players[turn % 2].field.ships) == 0:
                print(f"Победил {self.players[(turn - 1) % 2].NAME}")
                break


if __name__ == "__main__":
    print(
        "Перед вами игра Морской бой с компьютером")
    game = Game
    game.set_ships()
    game.move()
