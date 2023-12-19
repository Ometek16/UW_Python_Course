from Ułamek import Ułamek
import pytest


mult_data = [
                [Ułamek(1, 3), Ułamek(1, 2), Ułamek(1, 6)],
                [Ułamek(2, 1), Ułamek(2, 4), Ułamek(1, 1)],
                [Ułamek(3, 1), Ułamek(1, 2), Ułamek(3, 2)]
            ]

div_data = [
                [Ułamek(1, 3), Ułamek(1, 2), Ułamek(2, 3)],
                [Ułamek(2, 1), Ułamek(2, 4), Ułamek(4, 1)],
                [Ułamek(3, 1), Ułamek(1, 2), Ułamek(6, 1)]
           ]


def test_dodaj():
    a = Ułamek(1, 3)
    b = Ułamek(1, 2)
    c = Ułamek(5, 6)
    assert (a + b == c)


def test_odejmij():
    a = Ułamek(1, 3)
    b = Ułamek(1, 2)
    c = Ułamek(5, 6)
    assert (c - a == b)
    assert (c - b == a)


@pytest.mark.parametrize("a, b, expected", mult_data)
def test_mnożenie(a, b, expected):
    assert (a * b == expected)


@pytest.mark.parametrize("a, b, expected", div_data)
def test_dzielenie(a, b, expected):
    assert (a / b == expected)
