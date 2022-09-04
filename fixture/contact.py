
from model.contact import Contact
import re
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
            cells = row.find_elements_by_tag_name("td")
            id = cells[0].find_element_by_tag_name("input").get_attribute("value")
            all_phones = cells[5].text.splitlines()
            home=all_phones[0] if len(all_phones) > 0 else ""
            mobile = all_phones[1] if len(all_phones) > 1 else ""
            l.append(Contact(id=id, lastname=cells[1].text, firstname=cells[2].text, address=cells[3].text,
                             home=home, mobile=mobile, work="", fax=""))
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

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry") [index]
        cell = row.find_elements_by_tag_name("td") [7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry") [index]
        cell = row.find_elements_by_tag_name("td") [6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text=wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1) if "H: " in text else ""
        workphone = re.search("W: (.*)", text).group(1) if "W: " in text else ""
        mobilephone = re.search("M: (.*)", text).group(1) if "M: " in text else ""
        secondaryphone = re.search("P: (.*)", text).group(1) if "P: " in text else ""
        self.return_to_contact()
        return Contact(home=homephone, mobile=mobilephone,
                       work=workphone,  fax=secondaryphone)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        table = wd.find_element_by_id("maintable")
        row = table.find_elements_by_tag_name("tr")[index + 1]
        cols = row.find_elements_by_tag_name("td")
        cols[7].click()
        homephone =  wd.find_element_by_name("home").text
        workphone = wd.find_element_by_name("work").text
        mobilephone = wd.find_element_by_name("mobile").text
        secondaryphone = wd.find_element_by_name("fax").text
        self.return_to_contact()
        return Contact(home=homephone, mobile=mobilephone,
                       work=workphone,  fax=secondaryphone)



