import allure
import pytest

# 基础断言
def test_addition():
    assert 1 + 1 == 2, "加法运算失败"

# 类组织测试
class TestMathOperations:
    def test_multiplication(self):
        assert 2 * 3 == 6

# Fixture 使用
@pytest.fixture
def sample_list():
    return [1, 2, 3]

@pytest.fixture
def test_list_length(sample_list):  # PyCharm 会提示可用fixture
    assert len(sample_list) == 3

