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

    "Этот метода спрашивает игрока, хочет ли он расставить корабли на поле случайным образом."
    def wonder_set_auto(self):
        answer = str(input("Хотите ли вы расставить корабли случайным образом? Введите Да/Нет."))
        if answer == "Да":
            return True
        return False

    "Этот метод информирует игрока о доступном количестве кораблей разного типажа в данный момент времени."
    def inform_player(self):
        print(f"""Доступное количество кораблей
                четырёхпалубных : {HumanPLayer.SHIPS_NUM[4]};
                трёхпалубных : {HumanPLayer.SHIPS_NUM[3]};
                двухпалубных : {HumanPLayer.SHIPS_NUM[2]};
                однопалубных : {HumanPLayer.SHIPS_NUM[1]}. 
                """)

    """
    Этот метод позволяет игроку выбрать кораблю количество палуб из доступных.
    Если игрок вводит неправильное количество палуб, 
    или же корабль такого размера больше невозможно поставить,
    метод будет запрашивать количество палуб до тех пор, пока игрок не введет адекватное число. 
    """
    def set_sizes(self, i: int):
        size = int(input(f'Введите количество палуб у {i + 1}го корабля , который хотите добавить: '))
        while size not in HumanPLayer.SHIPS_NUM or HumanPLayer.SHIPS_NUM[size] == 0:
            print('Вы ввели недопустимое количество палуб или такой корабль больше невозможно поставить! '
                    'Попробуйте ещё раз.')
            size = int(input(f'Введите количество палуб у {i + 1}го корабля , который хотите добавить: '))
        return size

    def set_directions(self):
        # пока ещё не поняла, как работает расположение кораблей у Софьи.
        direction = int(input("""Укажите расположение вашего корабля относительно поля 
                                2 : горизонтально (бывшее вправо);
                                3 : вертикально (бывшее вниз)."""))
        while direction not in (2, 3):
            direction = int(input('Вы ввели неправильное направление у корабля! Попробуйте ещё раз: '))
        return direction

    def check_coord(self):
        coord_user = str(input('Укажите координату начала корабля:'))
        coord_computer = self.field.set_coord(coord_user)
        return coord_computer

    """ 
    Этот метод позволяет расставить корабли на поле вручную. 
    Пользователь вводит с клавиатуры данные о корабле.
    Если корабль можно добавить на поле, исключительных ситуаций не возникает.
    Иначе возникает ValueError.
    """
    def set_ships(self):
        self.field.print_my_field()
        if self.wonder_set_auto():
            self.set_randomly() 
            self.field.print_my_field()
        for ship in range(10):
            while True:
                self.inform_player()
                ship_size = self.set_sizes(ship)
                HumanPLayer.SHIPS_NUM[ship_size] -= 1
                ship_direction = self.set_directions()
                ship_coord = self.check_coord()
                added_ship = Ship(ship_coord, ship_direction, ship_size)
                try:
                    self.field.add_ship(added_ship)
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
        marked_cell = str(input('Введите номер клетки поля, куда будете стрелять: '))
        cell_int = opponent_field.set_coord(marked_cell)
        opponent_field.to_hit(cell_int)

    """
    Этот метод выводит на экран поле Игрока и поле Противника в данный момент игры.
    """
    def show_field(self, opponent_field: Field):
        print('Ваше поле: ')
        self.field.print_my_field()
        print('Поле противника:')
        opponent_field.print_opponent_field()
