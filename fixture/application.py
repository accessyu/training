from selenium import webdriver
from fixture.contact import ContactHelper
from fixture.session import SessionHelper
from fixture.group import GroupHelper

class Application:
    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "opera":
            self.wd = webdriver.Opera()
        else:
            raise ValueError("Unrecognised browser argument: %s" % browser)
        self.wd.implicitly_wait(3)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith('/addressbook/') and len(wd.find_elements_by_link_text("Last name")) > 0):
            wd.get(self.base_url)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()