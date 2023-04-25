import pytest
from calculadora.calc import soma, subtrai, divide, multiplica
from faker import Faker

faker = Faker()
x = faker.random_digit()
y = faker.random_digit()


def test_soma():
    assert soma(x, y) == x + y


def test_subtrai():
    assert subtrai(x, y) == x - y


@pytest.mark.skipif(y == 0, reason="Zero Division")
def test_divide():
    assert divide(x, y) == x / y


def test_multiplca():
    assert multiplica(x, y) == x * y


def test_zero_division():
    with pytest.raises(ValueError) as err:
        divide(1, 0)
    assert str(err.value) == 'Cannot divide by Zero'
