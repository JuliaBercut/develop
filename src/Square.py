from src.Figure import Figure


class Square(Figure):
    name = 'Square'

    def __init__(self, side_a):
        self._side_a = side_a

    @property
    def area(self):
        """The method used to calculate the area of a square"""
        return self._side_a ** 2

    @property
    def perimeter(self):
        """The method used to calculate the area of a square"""
        return self._side_a * 4
