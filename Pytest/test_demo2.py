import pytest


@pytest.mark.login
def test_m4():
    assert False


@pytest.mark.home
def test_m5():
    assert 100 == 100


@pytest.mark.login
def test_m6():
    assert "enver" == "Enver"


@pytest.mark.login
def test_login():
    assert "admin" == "admin"
