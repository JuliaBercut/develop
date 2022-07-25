from src.Figure import Figure


class Triangle(Figure):
    name = 'Triangle'

    def __init__(self, side_a, side_b, side_c):
        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c

        self._side_list = [self._side_a, self._side_b, self._side_c]
        self._the_largest_side_value = max([self._side_a, self._side_b, self._side_c])
        self._side_list.remove(self._the_largest_side_value)
        if self._the_largest_side_value >= sum(self._side_list):
            raise ValueError(
                "It is not possible to create a triangle with the specified sides' size")

    @property
    def area(self):
        """The method used to calculate the area of a triangle"""
        _p = (self._side_a + self._side_b + self._side_c) / 2
        return (_p * (_p - self._side_a) * (_p - self._side_b) * (_p - self._side_c)) ** 0.5

    @property
    def perimeter(self):
        """The method used to calculate the area of a triangle"""
        return self._side_a + self._side_b + self._side_c
