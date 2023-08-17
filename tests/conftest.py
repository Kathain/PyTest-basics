import pytest


@pytest.fixture(autouse=True)
def tc_setup():
    print("Launch browser")
    print("Login")
    print("Browse products")
    yield
    print("LogOff")
    print("Close browser")


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")