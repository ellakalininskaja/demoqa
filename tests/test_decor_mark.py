import pytest


@pytest.mark.smoke
def test_decor_mark1():
    assert True

@pytest.mark.regress
def test_decor_mark2():
    assert True

@pytest.mark.regress
def test_decor_mark3():
    assert True

@pytest.mark.regress
def test_decor_mark4():
    assert True

# pytest tests/test_decor_mark.py -m smoke
# pytest tests -m smoke

# pytest tests/test_decor_mark.py -m regress
# pytest tests -m regress
