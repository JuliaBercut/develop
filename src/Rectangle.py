from src.Figure import Figure


class Rectangle(Figure):
    name = 'Rectangle'

    def __init__(self, side_a, side_b):
        self._side_a = side_a
        self._side_b = side_b

    @property
    def area(self):
        """The method used to calculate the area of a rectangle"""
        return self._side_a * self._side_b

    @property
    def perimeter(self):
        """The method used to calculate the area of a rectangle"""
        return 2 * (self._side_a + self._side_b)
