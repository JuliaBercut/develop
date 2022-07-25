from abc import abstractmethod


class Figure:
    @property
    def name(self):
        """The attribute used to storage name of a figure"""
        raise NotImplementedError

    @property
    @abstractmethod
    def area(self):
        """The abstract method used to calculate the area of a figure"""
        pass

    @property
    @abstractmethod
    def perimeter(self):
        """The abstract method used to calculate the area of a figure"""
        pass

    def add_area(self, figure):
        """The method calculates the sum of area of the current figure and the passed figure"""
        if not (isinstance(figure, Figure)):
            raise ValueError
        else:
            return self.area + figure.area
