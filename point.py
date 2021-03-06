from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class Point:
    row: int
    col: int

    @staticmethod
    def from_string(coord: str):
        col_words = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']
        if coord[0] not in col_words:
            raise ValueError("Несоответствующее значение")
        col = col_words.index(coord[0]) + 1
        row = int(coord[1:len(coord)])
        if not 1 <= row <= 10:
            raise ValueError("Несоответствующее значение")
        return Point(row, col)
