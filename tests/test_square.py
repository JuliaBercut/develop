import pytest

from src.Square import Square


def test_name():
    """Check that an object has the attribute 'name'"""
    s = Square(side_a=1)
    assert hasattr(s, 'name') is True


def test_area():
    """Check of calculation of the 'area' attribute"""
    s = Square(side_a=3)
    assert s.area == 9


def test_perimeter():
    """Check of calculation of the 'perimeter' attribute"""
    s = Square(side_a=3)
    assert s.perimeter == 12


def test_add_area_positive():
    """Check of positive calculation of the 'add_area' method"""
    s1 = Square(side_a=4)
    s2 = Square(side_a=8)
    assert s1.add_area(s2) == 80


def test_add_area_negative():
    """Check of calculation of the 'add_area' method with parameter passed as non-Figure value"""
    with pytest.raises(ValueError):
        s1 = Square(side_a=4)
        s2 = str()
        s1.add_area(figure=s2)
