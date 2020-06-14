import yaml
import pytest


@pytest.mark.parametrize(("a", "b"), yaml.safe_load(open("./TestData.yml")))
class Test_Cal:
    def test_add(self, startCal, a, b):
        assert a + b == startCal.add(a, b)

    def test_sub(self, startCal, a, b):
        assert a - b == startCal.sub(a, b)

    def test_mul(self, startCal, a, b):
        assert a * b == startCal.mul(a, b)

    def test_div(self, startCal, a, b):
        if b == 0:
            raise Exception("除数不能为0")
        else:
            assert a / b == startCal.div(a, b)
