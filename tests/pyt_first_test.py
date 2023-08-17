import pytest

@pytest.mark.regression


def test_equal():
    assert 1 == 1, \
        "Its not equal to expected"


