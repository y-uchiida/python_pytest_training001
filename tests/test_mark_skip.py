import pytest


def test_something():
    assert True


@pytest.mark.skip(reason="not implemented")
def test_skipped():
    assert True
