from selenium.webdriver.common.by import By

from common.selenium_co import sel_click, sel_send_keys
from settings import ENV


class Event:

    def event_login(self,driver,username,password):
        driver.get(ENV.url)
        sel_click(driver, (By.XPATH, "//a[contains(text(), '登录')]"))
        sel_send_keys(driver, (By.XPATH, "//input[@placeholder='请输入用户名')]"),username)
        sel_send_keys(driver, (By.XPATH, "//input[@placeholder='请输入密码']"),password)
        sel_click(driver, (By.XPATH, "//input[@value='登录']]"))