from __future__ import annotations
from random import randint
from field import Field
from ship import Ship
from computer_player import ComputerPlayer
from human_player import HumanPLayer
from player import Player
from view import View
import ship_placement_view as spv


class Game:  # S: класс управляет игрой (вызов функции расстановки кораблей, очередность ходов)
    # O: причины для изменения: если игрок-человек будет играть не с компьютером, а с другим человеком
    players: list[Player]

    def __init__(self):
        self.spv = spv.ShipPlacementView(self.players[0].field)

        self.view = View(self.players[0].field, self.players[1].field)
        self.players = [HumanPLayer(self.spv, self.view), ComputerPlayer()]

    def set_ships(self):
        # спрашивает игрока-человека, как расставить корабли: рандомно или самостоятельно, в первом случае вызывает
        # метод класса игрока для расстановки кораблей, во втором случае вызывает метод для рандомной расстановки,
        # затем выводит поле и расставляет кораблик игрока-компьютера. Парметры: self, возвращаемых значений нет
        if self.view.set_ships() == 1:
            self.players[0].set_ships()
        else:
            self.players[0].set_randomly()
        self.view.print_owner_field()
        self.players[1].set_randomly()

    def move(self):
        # определяется, кто ходит первым. пока игра не закончена, в цикле по очереди вызывается метод move каждого из
        # игроков, после чего определяется победитель. Парметры: self, возвращаемых значений нет
        first_player = randint(1, 2)
        if first_player == 1:
            self.view.print_first_turn()
            turn = 0
        else:
            self.view.print_second_turn()
            turn = -1
        while len(self.players[0].field.ships) != 0 and len(self.players[1].field.ships) != 0:
            self.players[turn % 2].show_field(self.players[(turn - 1) % 2].field)
            self.players[turn % 2].move(self.players[(turn - 1) % 2].field)
            turn += 1
            if len(self.players[turn % 2].field.ships) == 0:
                self.view.print_winner(self.players[(turn - 1) % 2].NAME)
                break


if __name__ == "__main__":
    View.show_welcome_msg()
    game = Game()
    game.set_ships()
    game.move()
