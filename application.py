from selenium import webdriver


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def logout(self):
        wd = self.wd
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='New organization'])[1]/following::summary[1]").click()
        wd.find_element_by_xpath(
            "//button[@class='dropdown-item dropdown-signout']").click()

    def open_project_page(self):
        wd = self.wd
        # Открываем окно с проектами
        wd.get("https://github.com/")
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='New project'])[1]/following::summary[1]").click()
        wd.find_element_by_link_text("Your projects").click()
        wd.find_element_by_xpath("//main[@id='js-pjax-container']/div/div/div/div[2]/div/nav/a[2]").click()
        wd.find_element_by_link_text("barancev_training").click()

    def login(self, group):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_id("login_field").click()
        wd.find_element_by_id("login_field").clear()
        wd.find_element_by_id("login_field").send_keys(group.username)
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys(group.password)
        wd.find_element_by_name("commit").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("https://github.com/login")

    def destroy(self):
        self.wd.quit()
