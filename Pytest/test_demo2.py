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


# 1. pip install pytest pytest-xdist selenium
# 2. pytest -m login or py.test -m login Pytest/test_demo2.py
# To run tests with parallel execution, you can combine the -n option from pytest-xdist:
# 3. pytest -m login -n 4

