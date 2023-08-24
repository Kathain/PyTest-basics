import pytest

from random import randrange


@pytest.fixture
def get_number():
    return randrange(1, 100, 5)


def _calculate(a, b):   # это внутренняя функция в фикстурах
    return a + b


@pytest.fixture
def calculate():
    return _calculate  # тут ретерн возвращает именно вызов внутренней функции


@pytest.fixture
def make_number():
    print("I'm gettinng number")
    number = randrange(1, 1000, 3)
    yield number  # значит дальше работа продолжается в самом автотесте
    # yield number - передает номер в автотест
    print(f"Number at home {number}")
