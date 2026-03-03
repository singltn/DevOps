import pytest


def sample_add(a, b):
    return a + b


def test_add_positive_numbers():
    assert sample_add(2, 3) == 5


def test_add_negative_numbers():
    assert sample_add(-1, 1) == 0


def test_add_zero():
    assert sample_add(0, 0) == 0