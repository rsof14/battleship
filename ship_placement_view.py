<<<<<<< HEAD
from owner_field_view import OwnerFieldView
from field import Field
from human_player import HumanPLayer
=======
# from human_player import HumanPLayer
import human_player as hp

>>>>>>> 03b6852652588883731dfe09fe208814acf51121

class ShipPlacementView:
    def __init__(self, field: Field):
        self.view = OwnerFieldView(field)

    def print_field(self):
        self.view.print_field()

    "Этот метод спрашивает игрока, хочет ли он расставить корабли на поле случайным образом."

    def wonder_set_auto(self):
        return str(input("Хотите ли вы расставить корабли случайным образом? Введите Да/Нет."))

    "Этот метод информирует игрока о доступном количестве кораблей разного типажа в данный момент времени."

    def inform_player(self):
        print(f"""Доступное количество кораблей
                четырёхпалубных : {hp.HumanPLayer.SHIPS_NUM[4]};
                трёхпалубных : {hp.HumanPLayer.SHIPS_NUM[3]};
                двухпалубных : {hp.HumanPLayer.SHIPS_NUM[2]};
                однопалубных : {hp.HumanPLayer.SHIPS_NUM[1]}. 
                """)

    def enter_desk(self, i: int):
        return int(input(f'Введите количество палуб у {i + 1}го корабля , который хотите добавить: '))

    def enter_directions(self):
        return int(input("""Укажите расположение вашего корабля относительно поля 
                                1 : горизонтально;
                                2 : вертикально."""))

    def enter_coord(self):
        return str(input('Укажите координату начала корабля:'))

    def enter_hit_cell(self):
        return str(input('Введите номер клетки поля, куда будете стрелять: '))

    def show_error(error_message: str):
        print(error_message)
