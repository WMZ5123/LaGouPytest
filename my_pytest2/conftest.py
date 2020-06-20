import pytest
import yaml
from my_pytest2.my_cal import Cal


@pytest.fixture(autouse=True)
def StartCal():
    cal = Cal()
    print("开始计算")
    yield cal
    print("计算结束")


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="test", help="choose your environment: dev or test or st")


@pytest.fixture()
def cmdopt(request):
    data_path = "data_env.yml"
    myenv = request.config.getoption("--env", default="test")
    if myenv == "test":
        print("测试环境")
    if myenv == "dev":
        print("开发环境")
    if myenv == "st":
        print("集成环境")

    with open(data_path, "rb") as f:
        datas = yaml.safe_load(f)
        data = datas[myenv]
        return data
