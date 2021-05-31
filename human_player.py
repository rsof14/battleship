from player import Player
from field import Field
from ship import Ship
from computer_player import ComputerPlayer

class HumanPLayer(Player):
    # количесвто палуб: количество кораблей
    SHIPS_NUM = {'4' : 1, '3': 2, '2': 3, '1': 4} 

    def set_ships(self):
        self.field.print_my_field()
        ship_size = 0
        ship_direction = 0
        for i in range(10):
            while True:
                print(f"""Доступное количество 
                четырёхпалубных - {HumanPLayer.SHIPS_NUM['4']}, 
                трёхпалубных - {HumanPLayer.SHIPS_NUM['3']}, 
                двухпалубных - {HumanPLayer.SHIPS_NUM['2']},  
                однопалубных - {HumanPLayer.SHIPS_NUM['1']}. """)

                ship_size = int(input(f'Введите количество палуб у {i + 1}го корабля , который хотите добавить: '))
                while str(ship_size) not in HumanPLayer.SHIPS_NUM.keys() or HumanPLayer.SHIPS_NUM[str(ship_size)] == 0:
                    print('Вы ввели недопустимое количество палуб или такой корабль больше невозможно поставить! Попробуйте ещё раз: ')
                    ship_size = input(f'Введите количество палуб у корабля, который хотите добавить: ')
                if str(ship_size) in HumanPLayer.SHIPS_NUM.keys():
                    HumanPLayer.SHIPS_NUM[str(ship_size)] -= 1

                ship_direction = int(input('Укажите направление корабля (1 - вверх, 2 - вправо, 3 - вниз, 4 - вниз): '))
                while ship_direction not in (1, 2, 3, 4):
                    ship_direction = int(input('Вы ввели неправильное нарправление у корабля! Попробуйте ещё раз: '))

                start_coord = str(input('Укажите координату начала корабля: '))
                start_coord_int = self.field.set_coord(start_coord)
                ship = Ship(start_coord_int, ship_direction, ship_size)
                try:
                    self.field.add_ship(ship)
                except ValueError:
                    pass
                else:
                    break
                self.field.print_my_field()


    def move(self, opponent_field: Field):
        marked_cell = str(input('Введите номер клетки поля, куда будете стрелять: '))
        cell_int = opponent_field.set_coord(marked_cell)
        opponent_field.to_hit(cell_int)
        

    def show_field(self, opponent_field: Field):
        self.field.print_my_field()
        opponent_field.print_opponent_field()