from time import sleep
import pytest
from ec.types.regex import username
from selenium.webdriver.common.by import By

from common.selenium_co import sel_click, sel_send_keys
from common.sql import MysqlAuto
from po.event import Event
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

    def test_shopping_mall(self, username, password, result, open_page):
        driver = open_page
        driver.get(ENV.url)

        sel_click(driver, (By.XPATH, "//a[contains(text(), '登录')]"))
        sel_send_keys(driver, (By.XPATH, "//input[@placeholder='请输入用户名')]"),username)
        sel_send_keys(driver, (By.XPATH, "//input[@placeholder='请输入密码']"),password)
        sel_click(driver, (By.XPATH, "//input[@value='登录']]"))

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

    def test_shopping_mall_004(self,open_page):
        username = 'test_mall_004'
        pwd = 'test_mall_004'
        cpwd = 'test_mall_004'
        email = ('test_mall_004@qq.com')
        driver = open_page
        sel_click(driver, (By.XPATH, "//a[contains(text(), '注册')]"))

        sel_send_keys(driver, (By.XPATH, "//input[@id='user_name']"), username)
        sel_send_keys(driver, (By.XPATH, "//input[@id='pwd']"), pwd)
        sel_send_keys(driver, (By.XPATH, "//input[@id='cpwd']"), cpwd)
        sel_send_keys(driver, (By.XPATH, "//input[@id='email']"), email)

        sel_click(driver, (By.XPATH, "//input[@id='注 册']"))

        # 断言1： 查询用户表：是否存在该用户
        sql = [f'select * from df_user_userinfo where uname="{username}"']
        result = MysqlAuto().execute(sql)
        assert username in result[0]

        # 断言2： 检查是否正常登陆
        Event().event_login(driver, username, pwd)
        text = driver.find_element(By.XPATH, "//div[@class='login_btn fl']").text
        driver.find_element(By.XPATH, "//a[contains(text(), '退出')]").click()
        assert text == f"欢迎您：{username} | 退出"