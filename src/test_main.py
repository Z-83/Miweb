from main import Calculator


def test_suma():
    calculator = Calculator()
    assert calculator.suma(2, 2) == 4


def test_resta():
    calculator = Calculator()
    assert calculator.resta(5, 2) == 3