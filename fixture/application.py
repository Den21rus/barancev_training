from selenium import webdriver
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)


    def open_project_page(self):
        wd = self.wd
        # Открываем окно с проектами
        wd.get("https://github.com/")
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='New project'])[1]/following::summary[1]").click()
        wd.find_element_by_link_text("Your projects").click()
        wd.find_element_by_xpath("//main[@id='js-pjax-container']/div/div/div/div[2]/div/nav/a[2]").click()
        wd.find_element_by_link_text("barancev_training").click()


    def open_home_page(self):
        wd = self.wd
        wd.get("https://github.com/login")

    def destroy(self):
        self.wd.quit()
