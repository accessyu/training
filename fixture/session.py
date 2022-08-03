class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
            # logout
            wd = self.app.wd
            wd.find_element_by_link_text("Logout").click()

    def test_delete_first_group(app):
        app.open_home_page()
        app.session.login(username="admin", password="secret")
        app.group.delete_first_group()
        app.session.logout()