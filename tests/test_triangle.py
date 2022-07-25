import pytest

from src.Triangle import Triangle


def test_name():
    """Check that an object has the attribute 'name'"""
    t = Triangle(side_a=4, side_b=2, side_c=3)
    assert hasattr(t, 'name') is True


def test_area():
    """Check of calculation of the 'area' attribute"""
    t = Triangle(side_a=4, side_b=2, side_c=3)
    assert t.area == 2.9047375096555625


def test_perimeter():
    """Check of calculation of the 'perimeter' attribute"""
    t = Triangle(side_a=4, side_b=2, side_c=3)
    assert t.perimeter == 9


def test_zero_side():
    """Check of creation of a triangle with a zero size of at least one side"""
    with pytest.raises(ValueError):
        Triangle(side_a=0, side_b=1, side_c=1)


def test_negative_side():
    """Check of creation of a triangle with a negative size of at least one side"""
    with pytest.raises(ValueError):
        Triangle(side_a=-1, side_b=1, side_c=1)


def test_incorrect_sides():
    """Check of creation of a triangle with invalid combination of sides' size"""
    with pytest.raises(ValueError):
        Triangle(side_a=1, side_b=2, side_c=3)


def test_add_area_positive():
    """Check of positive calculation of the 'add_area' method"""
    t1 = Triangle(side_a=4, side_b=2, side_c=3)
    t2 = Triangle(side_a=8, side_b=2, side_c=9)
    assert t1.add_area(t2) == 10.2148332682622855


def test_add_area_negative():
    """Check of calculation of the 'add_area' method with parameter passed as non-Figure value"""
    with pytest.raises(ValueError):
        t1 = Triangle(side_a=4, side_b=2, side_c=3)
        t2 = str()
        t1.add_area(figure=t2)
