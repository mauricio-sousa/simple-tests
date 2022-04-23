from calculadora.calc import soma, subtrai, divide, multiplica
from faker import Faker

faker = Faker()
x = faker.random_digit()
y = faker.random_digit()


def test_soma():
    assert soma(x, y) == x + y


def test_subtrai():
    assert subtrai(x, y) == x - y


def test_divide():
    assert divide(x, y) == x / y


def test_multiplca():
    assert multiplica(x, y) == x * y
