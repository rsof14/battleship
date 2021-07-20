from player import Player
from field import Field
from ship import Ship
from ship_placement_view import ShipPlacementView
from view import View

"""
Класс Игрок-Человек, который отвечает за его ход и реализацию абстрактного класса Игрок. 
В методах move() и set_ships() человек сам определяет, куда выстрелить и как поставить корабли соответственно.
"""

class HumanPLayer(Player):
    SHIPS_NUM = [0, 4, 3, 2, 1]
    NAME = "Игрок - Человек"  # нужно, чтобы проще вывести победителя в Game.move

    # def __init__(self, spv: ShipPlacementView, view: View):
    #     self.spv = spv
    #     self.view = view

    def __init__(self, field: Field, view: View):
        super().__init__()
        self.spv = ShipPlacementView(field)
        self.view = view

        
    def auto_set(self):
        if self.spv.wonder_set_auto() == "Да":
            return True
        return False

    """
    Этот метод позволяет игроку выбрать кораблю количество палуб из доступных.
    Если игрок вводит неправильное количество палуб, 
    или же корабль такого размера больше невозможно поставить,
    метод будет запрашивать количество палуб до тех пор, пока игрок не введет адекватное число. 
    """
    def set_sizes(self, i: int):
        size = self.spv.enter_desk(i)
        while size not in HumanPLayer.SHIPS_NUM or HumanPLayer.SHIPS_NUM[size] == 0:
            self.spv.show_error('Вы ввели недопустимое количество палуб или такой корабль больше невозможно поставить! '
                    'Попробуйте ещё раз.')
            size = self.spv.enter_desk(i)
        return size

    def set_directions(self):
        direction = self.spv.enter_directions()
        while direction not in (2, 3):
            self.spv.show_error('Вы ввели неправильное направление у корабля! Попробуйте ещё раз: ')
            direction = self.spv.enter_directions()
        return direction

    def check_coord(self):
        coord_user = self.spv.enter_coord()
        coord_computer = self.field.set_coord(coord_user)
        return coord_computer

    """ 
    Этот метод позволяет расставить корабли на поле вручную. 
    Пользователь вводит с клавиатуры данные о корабле.
    Если корабль можно добавить на поле, исключительных ситуаций не возникает.
    Иначе возникает ValueError.
    """
    def set_ships(self):
        self.show_field()
        if self.auto_set():
            self.set_randomly() 
            self.show_field()
        for ship in range(10):
            while True:
                added_ship = self.create_ship(ship)
                try:
                    self.field.add_ship(added_ship)
                    self.show_field()
                except ValueError:
                    pass
                else:
                    break

    def create_ship(self, i: int):
        self.spv.inform_player()
        ship_size = self.set_sizes(i)
        HumanPLayer.SHIPS_NUM[ship_size] -= 1
        ship_direction = self.set_directions()
        ship_coord = self.check_coord()
        return Ship(ship_coord, ship_direction, ship_size)
        
    """
    Этот метод позволяет пользователю выбрать координату в поле противника, куда будет произведен выстрел.
    И, соответственно, выстреливает в указанную координату, если такой координат ещё не было.
    """
    def move(self, opponent_field: Field):
        marked_cell = self.spv.enter_hit_cell()
        cell_int = opponent_field.set_coord(marked_cell)
        opponent_field.to_hit(cell_int)

    """
    Этот метод выводит на экран поле Игрока и поле Противника в данный момент игры.
    """
    def show_field(self, opponent_field: Field):
        self.view.print_owner_field()
        self.view.print_opponent_field()
        #self.spv.view.print_field()

