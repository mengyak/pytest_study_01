import pytest
from selenium import webdriver

from common.log import log
from common.sql import MysqlAuto
from settings import ENV, DBSql


@pytest.fixture(scope="class")
def login():
    #打开浏览器和基本设置
    driver = webdriver.Chrome()
    log.debug('打开浏览器')
    driver.get(ENV.url)
    driver.maximize_window()
    log.debug('最大化窗口')
    driver.implicitly_wait(10) # 隐式等待，全局
    # 初始化数据
    MysqlAuto().execute(DBSql.sql_list)
    yield driver
    driver.quit()
    log.debug('关闭浏览器')