import pytest

from src.Rectangle import Rectangle


def test_name():
    """Check that an object has the attribute 'name'"""
    r = Rectangle(side_a=1, side_b=2)
    assert hasattr(r, 'name') is True


def test_area():
    """Check of calculation of the 'area' attribute"""
    r = Rectangle(side_a=1, side_b=2)
    assert r.area == 2


def test_perimeter():
    """Check of calculation of the 'perimeter' attribute"""
    r = Rectangle(side_a=1, side_b=2)
    assert r.perimeter == 6


def test_add_area_positive():
    """Check of positive calculation of the 'add_area' method"""
    r1 = Rectangle(side_a=1, side_b=2)
    r2 = Rectangle(side_a=4, side_b=3)
    assert r1.add_area(r2) == 14


def test_add_area_negative():
    """Check of calculation of the 'add_area' method with parameter passed as non-Figure value"""
    with pytest.raises(ValueError):
        r1 = Rectangle(side_a=1, side_b=2)
        r2 = str()
        r1.add_area(figure=r2)
4