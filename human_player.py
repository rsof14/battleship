from player import Player
from field import Field
from ship import Ship

"""
Класс Игрок-Человек, который отвечает за его ход и реализацию абстрактного класса Игрок. 
В методах move() и set_ships() человек сам определяет, куда выстрелить и как поставить корабли соответственно.
"""

class HumanPLayer(Player):
    SHIPS_NUM = [0, 4, 3, 2, 1]
    NAME = "Игрок - Человек"  # нужно, чтобы проще вывести победителя в Game.move

    """ 
    Этот метод позволяет расставить корабли на поле вручную. 
    Пользователь вводит с клавиатуры данные о корабле.
    Если корабль можно добавить на поле, исключительных ситуаций не возникает.
    Иначе возникает ValueError.
    """
    def set_ships(self):
        self.field.print_my_field()
        i = 1
        for available_size in range(len(HumanPLayer.SHIPS_NUM) - 1, 0, -1):
            for j in range(HumanPLayer.SHIPS_NUM[available_size]):
                while True:
                    print(f"""Доступное количество 
                    четырёхпалубных - {HumanPLayer.SHIPS_NUM[4]}, 
                    трёхпалубных - {HumanPLayer.SHIPS_NUM[3]}, 
                    двухпалубных - {HumanPLayer.SHIPS_NUM[2]},  
                    однопалубных - {HumanPLayer.SHIPS_NUM[1]}. """)

                    ship_size = int(input(f'Введите количество палуб у {i}го корабля , который хотите добавить: '))
                    while ship_size not in HumanPLayer.SHIPS_NUM or HumanPLayer.SHIPS_NUM[available_size] == 0:
                        print(
                            'Вы ввели недопустимое количество палуб или такой корабль больше невозможно поставить! '
                            'Попробуйте ещё раз.')
                        ship_size = input(f'Введите количество палуб у корабля, который хотите добавить: ')
                    HumanPLayer.SHIPS_NUM[ship_size] -= 1
                    i += 1

                    ship_direction = int(input('Укажите направление корабля (1 - вверх, 2 - вправо, 3 - вниз, 4 - влево): '))
                    while ship_direction not in (1, 2, 3, 4):
                        ship_direction = int(input('Вы ввели неправильное нарправление у корабля! Попробуйте ещё раз: '))
                    start_coord = str(input('Укажите координату начала корабля: '))
                    start_coord_int = self.field.set_coord(start_coord)
                    ship = Ship(start_coord_int, ship_direction, ship_size)
                    
                    try:
                        self.field.add_ship(ship)
                        self.field.print_my_field()
                    except ValueError:
                        pass
                    else:
                        break

    """
    Этот метод позволяет пользователю выбрать координату в поле противника, куда будет произведен выстрел.
    И, соответственно, выстреливает в указанную координату, если такой координат ещё не было.
    """
    def move(self, opponent_field: Field):
        already_hit = []
        marked_cell = str(input('Введите номер клетки поля, куда будете стрелять: '))
        while marked_cell in already_hit:
            print('вы уже стреляли в это поле! Попробуйте заново.')
            marked_cell = str(input('Введите номер клетки поля, куда будете стрелять: '))
        cell_int = opponent_field.set_coord(marked_cell)
        opponent_field.to_hit(cell_int)

    """
    Этот метод выводит на экран поле Игрока и поле Противника в данный момент игры.
    """
    def show_field(self, opponent_field: Field): # печать поля теперь из print
        print('Ваше поле: ')
        self.field.print_my_field()
        print('Поле противника:')
        opponent_field.print_opponent_field()
