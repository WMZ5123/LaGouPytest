import pytest
from my_pytest.my_cal import Cal


@pytest.fixture(autouse=True)
def startCal():
    cal = Cal()
    print("开始计算")
    yield cal
    print("计算结束")
