import re
from time import sleep


import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.log import log


@allure.step('鼠标左键单击')
def sel_click(driver, sel, timeout=20):
    try:
        WebDriverWait(driver, timeout).until(expected_conditions.element_to_be_clickable(sel)).click()
        sleep(0.2)
        selen = re.sub('[^\u4e00-\u9fa5]+', '', str(sel))
        if len(selen) > 0:
            log.debug(f"点击，{selen}")
        return True
    except Exception as e:
        log.error(f"无法定位到该元素，{sel}，异常为，\n{e}")
        raise e

@allure.step('元素可点击')
def elements_click(driver, by, sel, timeout=20):
    try:
        WebDriverWait(driver, timeout).until(expected_conditions.element_to_be_clickable((by, sel)))
        return True
    except Exception as e:
        log.error(f"已达到超时时间元素【{sel}】仍未加载出，不可点击，异常为{e}")
        raise e

@allure.step('元素可见')
def elements_visibility(driver, by, sel, timeout=20):
    try:
        WebDriverWait(driver, timeout).until(expected_conditions.visibility_of_element_located((by, sel)))
        return True
    except Exception as e:
        log.error(f"已达到超时时间元素仍然不可见，异常为{e}")
        raise e

@allure.step('输入内容')
def sel_send_keys(driver, sel, value, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(expected_conditions.element_to_be_clickable(sel)).click()
        sleep(0.2)
        WebDriverWait(driver, timeout).until(expected_conditions.element_to_be_clickable(sel)).send_keys(value)
        sleep(0.2)
        selen = re.sub('[^\u4e00-\u9fa5]', '', str(sel))
        if len(selen) > 0:
            log.debug(f"点击：{selen}，并输入值：{value}")
        return True
    except Exception as e:
        log.error(f"无法定位到该元素：{sel}，异常为：\n{e}")
        raise e

@allure.step('获取指定元素的text值')
def get_text(driver, els, timeout=10, mode=0):
    """获取指定元素的text值"""
    try:
        #等待元素在页面上出现
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_all_elements_located(els)
        )
        if mode == 0:
            log.debug(element.text)
            return element.text
        elif mode == 1:
            log.debug(element.get_attribute('textContent'))
            return element.get_attribute('textContent')
        return None
    except Exception as e:
        print(f"错误，{e}")
        return None
