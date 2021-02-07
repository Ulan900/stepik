import pytest

@pytest.mark.xfail(reason="bug in a 3rd party library")
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False