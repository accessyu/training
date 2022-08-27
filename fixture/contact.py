import self as self

from model.contact import Contact
class ContactHelper:
    contact_cache = None
    def __init__(self, app):
        self.app = app


  #  def open_contact_page(self):
   #     wd = self.app.wd
   #     wd.find_element_by_link_text("contact").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_add_contact_page()
        self.fill_contact_form(contact)
        wd.find_element_by_name("submit").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("address", contact.address)

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def return_to_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count(self):
        return len(self.get_contact_list())


    def get_contact_list(self):
        if self.contact_cache is not None:
            return self.contact_cache
        wd = self.app.wd
        l = []
        table = wd.find_element_by_id("maintable")
        rows = table.find_elements_by_tag_name("tr")
        for row in rows[1:]:
            cols = row.find_elements_by_tag_name("td")
            l.append(Contact(lastname=cols[1].text, firstname=cols[2].text, address=cols[3].text))
        self.contact_cache = l
        return l

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_id("11").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def modify_first_contact(self, contact):
        self.modify_contact_by_index(0, contact)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        table = wd.find_element_by_id("maintable")
        row = table.find_elements_by_tag_name("tr")[index+1]
        cols = row.find_elements_by_tag_name("td")
        cols[7].click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.return_to_contact()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        table = wd.find_element_by_id("maintable")
        row = table.find_elements_by_tag_name("tr")[index + 1]
        cols = row.find_elements_by_tag_name("td")
        cols[0].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None






