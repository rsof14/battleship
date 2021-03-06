from random import randint
from point import Point
from field import Field
from player import Player

"""
Класс Игрок-Компьтер, который отвечает за его ход и реализацию абстрактного класса Игрок. 
Здесь методы move() и set_ships() определяются рандомом.
"""

class ComputerPlayer(Player):
    NAME = "Компьютер"  # нужно, чтобы проще вывести победителя в Game.move

    def __init__(self):
        super().__init__()
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
        row = randint(1, 10)
        col = randint(1, 10)
        point = str(row) + str(col)
        while point in already_hit:        
            row = randint(1, 10)
            col = randint(1, 10)
            point = str(row) + str(col)
        opponent_field.to_hit(Point(row, col))
        already_hit.append(point)

    def show_field(self): # печать поля теперь из print
        pass
