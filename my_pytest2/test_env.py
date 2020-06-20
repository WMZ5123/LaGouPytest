import pytest


def test_env(cmdopt):
    print(f"{cmdopt}")


if __name__ == "__main__":
    pytest.main(["-s", "--env=test", "test_env.py"])
