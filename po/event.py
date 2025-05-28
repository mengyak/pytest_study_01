from selenium.webdriver.common.by import By

from common.log import log
from common.selenium_co import sel_click, sel_send_keys
from settings import ENV


class Event:

    def event_login(self,driver,username,password):
        try:
            driver.get(ENV.url)
            sel_click(driver, (By.XPATH, "//a[contains(text(), '登录')]"))
            sel_send_keys(driver, (By.XPATH, "//input[@placeholder='请输入用户名')]"),username)
            sel_send_keys(driver, (By.XPATH, "//input[@placeholder='请输入密码']"),password)
            sel_click(driver, (By.XPATH, "//input[@value='登录']]"))
        except Exception as e:
            log.error(f'登录异常，为{e}')
            raise e

    def event_register(self,driver,user_name,pwd,cpwd,email):
        try:
            driver.get(ENV.url)
            sel_click(driver, (By.XPATH, "//a[contains(text(), '注册')]"))
            sel_send_keys(driver, (By.XPATH, "//input[@id='user_name']"), user_name)
            sel_send_keys(driver, (By.XPATH, "//input[@id='pwd']"), pwd)
            sel_send_keys(driver, (By.XPATH, "//input[@id='cpwd']"), cpwd)
            sel_send_keys(driver, (By.XPATH, "//input[@id='email']"), email)
            sel_click(driver, (By.XPATH, "//input[@id='注 册']"))
        except Exception as e:
            log.error(f'注册异常，为{e}')
            raise e