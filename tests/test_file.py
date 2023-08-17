import pytest


def test_Login():
    print('Login Successful')


@pytest.mark.skip
def test_LogOff():
    print('LogOff Successful')


def test_Calculation():
    print('Calculation Successful')

@pytest.mark.xfail
def test_Calculation1():
    print('Calculation1 Successful')


def test_Calculation_city():
    print('Calculation of cities is Successful')
