from calculadora.calc import soma, subtrai, divide, multiplica
from faker import Faker
from ward import raises, test, skip


faker = Faker()
x = faker.random_digit()
y = faker.random_digit()


@test("simple addition")
def test_soma():
    assert soma(x, y) == x + y

@test("simple subtraction")
def test_subtrai():
    assert subtrai(x, y) == x - y

@test("Skipped Zero Division")
@skip("Skipped Zero Division", when=y == 0)
def test_divide():
    assert divide(x, y) == x / y

@test("simple multiplication")
def test_multiplicacao():
    assert multiplica(x, y) == x * y
 
@test("a ZeroDivision error is raised when we divide by 0")
def test_zero_division():
    with raises(ZeroDivisionError):
        1 / 0    