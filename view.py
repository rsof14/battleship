from opponent_field_view import OpponentFieldView
from owner_field_view import OwnerFieldView
from field import Field


def show_welcome_msg():
    print("Перед вами игра Морской бой с компьютером")


class View:
    def __init__(self, owner_field: Field, opponent_field: Field):
        self.owner_field = OwnerFieldView(owner_field)
        self.opponent_field = OpponentFieldView(opponent_field)

    # def show_welcome_msg(self):
    #     print("Перед вами игра Морской бой с компьютером")

    def set_ships(self):
        return int(input('нажмите 1, чтобы расставить корабли самостоятельно, нажмите 2, '
                         'чтобы расставить корабли в случайном порядке'))

    def print_owner_field(self):
        self.owner_field.print_field()

    def print_opponent_field(self):
        self.opponent_field.print_field()

    def print_first_turn(self):
        print("Случайным образом выбрано: вы ходите первыми")

    def print_second_turn(self):
        print("Случайным образом выбрано: компьютер ходит первым")

    def print_winner(self, winner_name: str):
        print(f"Победил {winner_name}")
