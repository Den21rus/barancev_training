
class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, group):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_id("login_field").click()
        wd.find_element_by_id("login_field").clear()
        wd.find_element_by_id("login_field").send_keys(group.username)
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys(group.password)
        wd.find_element_by_name("commit").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='New organization'])[1]/following::summary[1]").click()
        wd.find_element_by_xpath(
            "//button[@class='dropdown-item dropdown-signout']").click()

