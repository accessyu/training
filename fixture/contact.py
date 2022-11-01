from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re

class ContactHelper:
    def __init__(self, app):
        self.app = app


    def create(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # Init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # Submit addition
        wd.find_element_by_name("submit").click()
        self.contact_cache = None

    def add_contact_to_group(self, id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        # Choose group from drop list for contact addition
        wd.find_element_by_xpath("//select[@name='to_group']//option[@value='%s']" %group_id).click()
        # Submit addition
        wd.find_element_by_name("add").click()
        # Go to chosen group page
        wd.find_element_by_xpath("//a[@href='./?group=%s']" %group_id).click()
        self.contact_cache = None

    def remove_contact_from_group(self, id,  group_id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_group_to_display_contacts(group_id)
        self.select_contact_by_id(id)
        # Submit removal
        wd.find_element_by_name("remove").click()
        # Go to chosen group page
        wd.find_element_by_xpath("//a[@href='./?group=%s']" %group_id).click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.filling_condition_check("firstname", contact.firstname)
        self.filling_condition_check("middlename", contact.middlename)
        self.filling_condition_check("lastname", contact.lastname)
        self.filling_condition_check("nickname", contact.nickname)
        self.filling_condition_check("title", contact.title)
        self.filling_condition_check("company", contact.company)
        self.filling_condition_check("address", contact.address)
        self.filling_condition_check("home", contact.home_phone)
        self.filling_condition_check("mobile", contact.cell_phone)
        self.filling_condition_check("work", contact.work_phone)
        self.filling_condition_check("fax", contact.fax)
        self.filling_condition_check("email", contact.email_1)
        self.filling_condition_check("email2", contact.email_2)
        self.filling_condition_check("email3", contact.email_3)
        self.filling_condition_check("homepage", contact.homepage)
        self.filling_condition_check("bday", contact.day)
        self.filling_condition_check("bmonth", contact.month)
        self.filling_condition_check("byear", contact.year)
        self.filling_condition_check("aday", contact.a_day)
        self.filling_condition_check("amonth", contact.a_month)
        self.filling_condition_check("ayear", contact.a_year)
        self.filling_condition_check("address2", contact.address2)
        self.filling_condition_check("phone2", contact.secondary_phone)
        self.filling_condition_check("notes", contact.notes)

    def filling_condition_check(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            if field_name == "bday" or \
                    field_name == "bmonth" or \
                    field_name == "aday" or \
                    field_name == "amonth":
                wd.find_element_by_name(field_name).click()
                Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
                # wd.find_element_by_name(field_name).click()
            else:
                wd.find_element_by_name(field_name).click()
                wd.find_element_by_name(field_name).clear()
                wd.find_element_by_name(field_name).send_keys(text)
        else:
            pass


    def delete(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # Submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.open_home_page()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@id='%s']" %id).click()

    def edit(self):
        self.edit_by_index(0)

    def edit_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.find_edit_button_by_index(index)
        self.fill_contact_form(new_contact_data)
        # Submit update
        wd.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
        self.contact_cache = None

    def edit_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.find_edit_button_by_id(id)
        self.fill_contact_form(new_contact_data)
        # Submit update
        wd.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
        self.contact_cache = None


    def find_edit_button_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def find_edit_button_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[@href ='edit.php?id=%s']" %id).click()

    def select_group_to_display_contacts(self, group_id):
        wd = self.app.wd
        wd.find_element_by_xpath("//select[@name='group']//option[@value='%s']" %group_id).click()



    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))


    contact_cache = None
    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name = 'entry']"):
                cells = element.find_elements_by_tag_name("td")
                lastname_text = cells[1].text
                firstname_text = cells[2].text
                address_text = cells[3].text
                id = element.find_element_by_name("selected[]").get_attribute("id")
                all_mails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(lastname=lastname_text, firstname=firstname_text, id=id,
                                                  address=address_text, all_mails=all_mails, all_phones=all_phones))
        return list(self.contact_cache)


    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.find_edit_button_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email_1 = wd.find_element_by_name("email").get_attribute("value")
        email_2 = wd.find_element_by_name("email2").get_attribute("value")
        email_3 = wd.find_element_by_name("email3").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        cell_phone = wd.find_element_by_name("mobile").get_attribute("value")
        secondary_phone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address, email_1=email_1,
                       email_2=email_2, email_3=email_3, home_phone=home_phone, cell_phone=cell_phone,
                       work_phone=work_phone, secondary_phone=secondary_phone)


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        cell_phone = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        secondary_phone = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, cell_phone=cell_phone,
                       work_phone=work_phone, secondary_phone=secondary_phone)

    def get_contact_list_from_group_page(self,id):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page
            self.select_group_to_display_contacts(id)
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name = 'entry']"):
                cells = element.find_elements_by_tag_name("td")
                lastname_text = cells[1].text
                firstname_text = cells[2].text
                id = element.find_element_by_name("selected[]").get_attribute("id")
                self.contact_cache.append(Contact(lastname=lastname_text, firstname=firstname_text, id=id))
        return list(self.contact_cache)


    def delete_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        # Submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.open_home_page()
        self.contact_cache = None



    def clear(self, s):
        return re.sub("[() /.-]", "", s)

    def merge_info_like_on_home_page(self, contact, info_type):
        if info_type == 'mail':
            return "\n".join(filter(lambda x: x != "",
                                    filter(lambda x: x is not None,
                                        [contact.email_1, contact.email_2, contact.email_3])))

        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.home_phone, contact.cell_phone, contact.work_phone,
                                            contact.secondary_phone]))))

