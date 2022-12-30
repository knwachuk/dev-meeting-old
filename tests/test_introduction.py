import pytest


def inc(x: int) -> int:
    return x + 1


def dec(x: int) -> int:
    return x - 1


def test_inc():
    assert inc(3) == 4


def test_dec():
    assert dec(4) == 3
