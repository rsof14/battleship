from random import randint

from field import Field
from player import Player

"""
Класс Игрок-Компьтер, который отвечает за его ход и реализацию абстрактного класса Игрок. 
Здесь методы move() и set_ships() определяются рандомом.
"""

class ComputerPlayer(Player):
    NAME = "Компьютер"  # нужно, чтобы проще вывести победителя в Game.move

    def __init__(self):
        self.already_hit = []

    """
    Этот метод случайным образом производит расстановку кораблей.
    """
    def set_ships(self):
        self.set_randomly()

    """
    Этот метод случайным образом выбирает координату в поле противника, куда стрелять.
    И, соответственно, стреляет по указанной координате.
    """
    def move(self, opponent_field: Field):
        already_hit = [] 
        row = randint(0, 9)
        col = randint(0, 9)
        point = str(row) + str(col)
        while point in already_hit:        
            row = randint(0, 9)
            col = randint(0, 9)
            point = str(row) + str(col)
        opponent_field.to_hit([row, col])
        already_hit.append(point)

    def show_field(self, opponent_field: Field): # печать поля теперь из print
        pass
