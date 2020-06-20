import pytest
import yaml

test_data = yaml.safe_load(open('./TestData.yml', 'rb'))


class TestCal():
    @pytest.mark.dependency(name='add')
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a, b", test_data['add'])
    def test_add(self, a, b, StartCal):
        assert StartCal.add(a, b) == a + b

    @pytest.mark.dependency(depends=['add'])
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a, b", test_data['sub'])
    def test_sub(self, a, b, StartCal):
        assert StartCal.sub(a, b) == a - b

    @pytest.mark.dependency(name='mul')
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a, b", test_data['mul'])
    def test_mul(self, a, b, StartCal):
        assert StartCal.mul(a, b) == a * b

    @pytest.mark.dependency(depends=['mul'])
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("a, b", test_data['div'])
    def test_div(self, a, b, StartCal):
        assert StartCal.div(a, b) == a / b

    if __name__ == '__main__':
        pytest.main()
