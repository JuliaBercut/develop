import pytest

from src.Circle import Circle


def test_name():
    """Check that an object has the attribute 'name'"""
    c = Circle(radius=5)
    assert hasattr(c, 'name') is True


def test_area():
    """Check of calculation of the 'area' attribute"""
    c = Circle(radius=5)
    assert c.area == 78.53981633974483


def test_perimeter():
    """Check of calculation of the 'perimeter' attribute"""
    c = Circle(radius=5)
    assert c.perimeter == 31.41592653589793


def test_add_area_positive():
    """Check of positive calculation of the 'add_area' method"""
    c1 = Circle(radius=4)
    c2 = Circle(radius=7)
    assert c1.add_area(c2) == 204.20352248333654


def test_add_area_negative():
    """Check of calculation of the 'add_area' method with parameter passed as non-Figure value"""
    with pytest.raises(ValueError):
        c1 = Circle(radius=2)
        c2 = str()
        c1.add_area(figure=c2)
