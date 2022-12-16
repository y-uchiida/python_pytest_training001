import pytest


@pytest.mark.fooGroup
def test_sample_foo1():
    assert True


@pytest.mark.fooGroup
def test_sample_foo2():
    assert True


@pytest.mark.fooGroup
def test_sample_foo3():
    assert True


@pytest.mark.fooGroup
class TestFooClassSample:
    @pytest.mark.fooClassGroup
    def test_fooclass(self):
        assert True


@pytest.mark.barGroup
def test_sample_bar1():
    assert True


@pytest.mark.barGroup
def test_sample_bar2():
    assert True


@pytest.mark.barGroup
def test_sample_bar3():
    assert True


@pytest.mark.barGroup
class TestBarClassSample:
    @pytest.mark.barClassGroup
    def test_barclass(self):
        assert True
