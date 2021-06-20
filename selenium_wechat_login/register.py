#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Register:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def register(self):
        self._driver.find_element_by_id('corp_name').send_keys('htllo222')
        self._driver.find_element_by_id('manager_name').send_keys("hello1111")
        time.sleep(5)
        self._driver.quit()
        return True
