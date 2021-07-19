from human_player import HumanPLayer

class ShipPlacementView:
    def __init__(self) -> None:
        pass

    "Этот метод спрашивает игрока, хочет ли он расставить корабли на поле случайным образом."
    def wonder_set_auto(self):
        return str(input("Хотите ли вы расставить корабли случайным образом? Введите Да/Нет."))         

    "Этот метод информирует игрока о доступном количестве кораблей разного типажа в данный момент времени."
    def inform_player(self):
        print(f"""Доступное количество кораблей
                четырёхпалубных : {HumanPLayer.SHIPS_NUM[4]};
                трёхпалубных : {HumanPLayer.SHIPS_NUM[3]};
                двухпалубных : {HumanPLayer.SHIPS_NUM[2]};
                однопалубных : {HumanPLayer.SHIPS_NUM[1]}. 
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
