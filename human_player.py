from player import Player
from field import Field
from ship import Ship
from computer_player import ComputerPlayer

class HumanPLayer(Player):
    # количесвто палуб: количесвто кораблей
    SHIPS_NUM = {'4' : 1, '3': 2, '2': 3, '1': 4} 

    def set_ships(self):
        self.field.print_my_field()
        for i in range(10):
            ship_size = int(input(f'Введите количество палуб у {i + 1}го корабля , который хотите добавить: '))
            print('Доступное количество четырёхпалубных - {0}, '+ 
                'трёхпалубных - {1}, ' + 
                'двухпалубных - {2}, ' + 
                'однопалубных - {3}'.format(self.SHIPS_NUM['4'], self.SHIPS_NUM['3'], self.SHIPS_NUM['2'], self.SHIPS_NUM['1']))
            # Спросить про "try - except KeyError"
            if str(ship_size) in self.SHIPS_NUM.keys():
                self.SHIPS_NUM[str(ship_size)] -= 1
            ship_direction = int(input('Укажите направление корабля: (1 - вверх, 2 - вправо, 3 - вниз, 4 - вверх)'))
            start_coord = int(input('Укажите координату начала корабля: '))
            ship = Ship(start_coord, ship_direction, ship_size, [])
            self.field.add_ship(ship)
            self.field.print_my_field()


    def move(self):
        row = 0
        col = 0
        marked_cell = str(input('Введите номер клетки поля, куда будете бить: '))
        # тут немного не так, надо подумать лучше
        if marked_cell in self.field.hits_misses:
            print('Ход в эту точку уже был!')
        else:
            for i in range(10):
                # тут я полагаю, что есть некая костанта у field, отвечающая за АБВГДЕЖЗИК
                if marked_cell[0] == self.field.alphabet[i]: 
                    row = i
                    col = int(marked_cell[1] -1)
            if self.ComputerPlayer.field[row][col] == ' ':
                print('Вы не попали!')
                self.ComputerPlayer.field[row][col] = '.'
            else:
                print('Вы попали!')
                self.ComputerPlayer.field[row][col] = 'x'
                # обратиться к кораблю ПРОТИВНИКА и изменить его hits
        

    def show_field(self, opponent_field: Field):
        self.field.print_my_field()
        opponent_field.print_opponent_field()