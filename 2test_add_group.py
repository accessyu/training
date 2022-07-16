# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group
from application import Application

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Application ()

    def test_add_group(self):
        self.login(username="admin",password="secret")
        self.create_group(Group(name="123", header="123"))
        self.logout()

    def test_add_empty_group(self):
        self.login(username="admin", password="secret")
        self.create_group(Group(name="", header="", footer=""))
        self.logout()
    
    def tearDown(self):
        self.app.destroy()

if __name__ == "__main__":
    unittest.main()
