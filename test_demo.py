#!/usr/bin/env python
# -*- coding:utf-8 -*-
import shelve

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo():
    def setup_method(self, method):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()

        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_demo(self):
        # print(self.driver.get_cookies())
        db = shelve.open("cookies")
        # db['cookie'] = self.driver.get_cookies()
        cookies = db['cookie']


        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # self.driver.find_element(By.LINK_TEXT, "通讯录").click()
        # self.driver.find_element_by_id('menu_contacts').click()
        self.driver.implicitly_wait(5)
