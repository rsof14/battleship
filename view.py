from opponent_field_view import OpponentFieldView
from owner_field_view import OwnerFieldView
from field import Field


def welcome_msg():
    print("Перед вами игра Морской бой с компьютером")


def set_ships():
    return int(input('нажмите 1, чтобы расставить корабли самостоятельно, нажмите 2, '
                     'чтобы расставить корабли в случайном порядке'))


def print_owner_field(field: Field):
    OwnerFieldView(field).print_my_field()


def print_opponent_field(field: Field):
    OpponentFieldView(field).print_opponent_field()


def first_turn():
    print("Случайным образом выбрано: вы ходите первыми")


def second_turn():
    print("Случайным образом выбрано: компьютер ходит первым")


def print_winner(winner_name: str):
    print(f"Победил {winner_name}")
