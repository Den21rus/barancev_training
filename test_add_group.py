# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(executable_path=r'')
        self.wd.implicitly_wait(30)
    
    def test_add_group(self):
        wd = self.wd
        wd.get("https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fsignup%3Fref_cta%3DSign%2Bup%26ref_loc%3Dheader%2Blogged%2Bout%26ref_page%3D%252F%253Cuser-name%253E%252F%253Crepo-name%253E%26source%3Dheader-repo%26source_repo%3DDen21rus%252Fbarancev_training")
        wd.find_element_by_id("login_field").click()
        wd.find_element_by_id("login_field").clear()
        wd.find_element_by_id("login_field").send_keys("Den21rus")
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys("Htc777@pux")
        wd.find_element_by_xpath("//div[@id='login']/div[4]").click()
        wd.find_element_by_name("commit").click()
        wd.get("https://github.com/")
        wd.find_element_by_xpath("//div[@id='repos-container']/ul/li/div/div/a/span").click()
    
    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
