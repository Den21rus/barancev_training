# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import Group


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, Group(username="Den21rus", password="Htc777@pux"))
        self.open_project_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='New organization'])[1]/following::summary[1]").click()
        wd.find_element_by_xpath(
            "//button[@class='dropdown-item dropdown-signout']").click()

    def open_project_page(self, wd):
        # Открываем окно с проектами
        wd.get("https://github.com/")
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='New project'])[1]/following::summary[1]").click()
        wd.find_element_by_link_text("Your projects").click()
        wd.find_element_by_xpath("//main[@id='js-pjax-container']/div/div/div/div[2]/div/nav/a[2]").click()
        wd.find_element_by_link_text("barancev_training").click()

    def login(self, wd, group):
        wd.find_element_by_id("login_field").click()
        wd.find_element_by_id("login_field").clear()
        wd.find_element_by_id("login_field").send_keys(group.username)
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys(group.password)
        wd.find_element_by_name("commit").click()

    def open_home_page(self, wd):
        wd.get("https://github.com/login")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.wd.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.wd.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
