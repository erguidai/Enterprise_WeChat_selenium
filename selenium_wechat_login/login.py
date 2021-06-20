#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_wechat_login.register import Register


class Login:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        # self._driver.find_element()

    def scanf(self):
        pass

    def goto_register(self):
        # self._driver.find_element_by_css_selector('login_registerBar_link').click()
        self._driver.find_element_by_xpath('//*[@id="wework_admin.loginpage_wx_$"]/main/div[2]/a').click()
        return Register(self._driver)
