from math import pi

from src.Figure import Figure


class Circle(Figure):
    name = 'Circle'

    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        """The method used to calculate the area of a circle"""
        return pi * self._radius ** 2

    @property
    def perimeter(self):
        """The method calculates the perimeter of a circle"""
        return 2 * pi * self._radius
