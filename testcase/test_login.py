from time import sleep
import pytest
from selenium.webdriver.common.by import By

from settings import ENV


class TestLogin:
    @pytest.mark.parametrize('username, password, result', [
        ('test123456', 'test123456', "欢迎您, test123456 | 退出"),
        ('bucunzai', 'test123456', '用户名错误'),
        ('test123456', 'cuowu', '密码错误')
    ], ids=(
        'test_shopping_mall_001',
        'test_shopping_mall_002',
        'test_shopping_mall_003'
    ))
    def test_shopping_mall(self, username, password, result, login):
        driver = login()
        driver.get(ENV.url)
        driver.find_element(By.XPATH, "//a[contains(text(), '登录')]").click()
        driver.find_element(By.XPATH, "//input[@placeholder='请输入用户名')]").send_keys(username)
        driver.find_element(By.XPATH, "//input[@placeholder='请输入密码']]").send_keys(password)
        driver.find_element(By.XPATH, "//input[@value='登录']]").click()
        sleep(1)

        if '欢迎您' in result:
            text = driver.find_element(By.XPATH, "//div[@class='login_btn fl']").text
            driver.find_element(By.XPATH, "//a[contains(text(), '退出')]").click()
            assert text == result

        elif '用户名作物' in result:
            text = driver.find_element(By.XPATH, "//div[@class='user_error']").text
            assert text == "用户名错误"
        elif '密码错误' in result:
            text = driver.find_element(By.XPATH, "//div[@class='pwd_error']").text
            assert text == "密码错误"