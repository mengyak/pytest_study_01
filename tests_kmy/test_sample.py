import pytest


def test_addition():
    assert 1 + 1 == 2

@pytest.mark.parametrize("input,expected", [("3+5", 8), ("2 * 4", 8)])
def test_eval(input, expected):
    assert eval(input) == expected

@pytest.mark.parametrize("name", ["Alice", "Bob"])
def test_greet(name):
    assert name in ["Alice", "Bob", "Charlie"]

# test_sample.py
def test_allure_demo():
    assert True


