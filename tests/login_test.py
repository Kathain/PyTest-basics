import pytest


def test_login():
    print("Login")


def test_Log_off():
    print("Logoff successful")

@pytest.mark.sanity
def test_calculation():
    assert 2 + 2 == 6
