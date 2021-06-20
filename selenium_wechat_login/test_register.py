#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium_wechat_login.index import Index


class TestRegister:
    def setup(self):
        self.index = Index()

    def test_register(self):
        self.index.goto_login().goto_register().register()

        # self.index.goto_register()