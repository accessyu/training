from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_add_form(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        #wd.get("http://localhost/addressbook/edit.php")


    def fill_contact_form(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address_1)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.phone_home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_home)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.phone_work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email_1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email_2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email_3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        if contact.bmonth != '':
            wd.find_element_by_name("bmonth").click()
            Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        if contact.amonth != '':
            wd.find_element_by_name("amonth").click()
            Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address_2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone_home_2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)


    def create_contact(self, contact):
        self.open_contact_add_form()
        self.fill_contact_form(contact)
        self.enter_contact_creation()
        self.retern_to_home_page()
        self.contact_cache = None


    def retern_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        #wd.get("http://localhost/addressbook/")


    def enter_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.retern_to_home_page()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.retern_to_home_page()
        self.contact_cache = None  # сбрасываем кеш, при следующем обращении к get_contact_list будет стоиться заново в этом методе


    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.retern_to_home_page()
        self.contact_cache = None


    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()


    def delete_first_contact(self):
        self.delete_contact_by_index(0) #удаляем первый контакт (счет всегда идет с 0)


    def modify_contact_by_indeх(self, index, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        #wd.get("http://localhost/addressbook/edit.php?id=5")
        # update contact form
        self.fill_contact_form(new_contact_data)
        # submit edit
        wd.find_element_by_name("update").click()
        #wd.get("http://localhost/addressbook/edit.php")
        self.retern_to_home_page()
        self.contact_cache = None  # сбрасываем кеш, при следующем обращении к get_contact_list будет строиться заново в этом методе


    def modify_contact_by_id(self, new_contact_data, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector("tr[name='entry'] a[href='edit.php?id=%s'" % id).click()
        #wd.get("http://localhost/addressbook/edit.php?id=5")
        # update contact form
        self.fill_contact_form(new_contact_data)
        # submit edit
        wd.find_element_by_name("update").click()
        #wd.get("http://localhost/addressbook/edit.php")
        self.retern_to_home_page()
        self.contact_cache = None


    def modify_first_contact(self):
        self.modify_contact_by_indeх(0)

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))


    #def get_contact_list(self):
        #wd = self.app.wd
        #self.app.open_home_page()
        #contacts = []
        #elements = wd.find_elements_by_css_selector("#maintable > tbody > tr")[1:]
       # for element in elements:
            #id = element.find_element_by_css_selector("input").get_attribute('id')
            #contacts.append(Contact(id=id))
        #return contacts

    contact_cache = None


    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            elements = wd.find_elements_by_css_selector("tr[name=entry]")
            for element in elements:
                cells = element.find_elements_by_tag_name("td")
                name = cells[2].text
                lastname = cells[1].text
                address_1 = cells[3].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(name=name, lastname=lastname, id=id, address_1=address_1,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)


    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        phone_home = re.search("H: (.*)", text).group(1)
        mobile_home = re.search("M: (.*)", text).group(1)
        phone_work = re.search("W: (.*)", text).group(1)
        phone_home_2 = re.search("P: (.*)", text).group(1)
        return Contact(phone_home=phone_home, mobile_home=mobile_home,
                       phone_work=phone_work, phone_home_2=phone_home_2)


    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()


    ##def get_contact_info_from_edit_page(self, index):
       ## wd = self.app.wd
        ##self.app.open_home_page()
        ##self.open_contact_to_edit_by_index(index)
        ##name = wd.find_element_by_name("firstname").get_attribute("value")
       ## lastname = wd.find_element_by_name("lastname").get_attribute("value")
       ## id = wd.find_element_by_name("id").get_attribute("value")
       ## phone_home = wd.find_element_by_name("home").get_attribute("value")
        ##mobile_home = wd.find_element_by_name("mobile").get_attribute("value")
        ##phone_work = wd.find_element_by_name("work").get_attribute("value")
        ##phone_home_2 = wd.find_element_by_name("phone2").get_attribute("value")
        ##address_1 = wd.find_element_by_name('address').get_attribute('value')
        ##email_1 = wd.find_element_by_name('email').get_attribute('value')
        ##email_2 = wd.find_element_by_name('email2').get_attribute('value')
        ##email_3 = wd.find_element_by_name('email3').get_attribute('value')
        #return Contact(name=name, lastname=lastname, id=id,
                       #phone_home=phone_home, mobile_home=mobile_home,
                       #phone_work= phone_work, phone_home_2=phone_home_2,
                       #address_1=address_1,
                       #email_1=email_1, email_2=email_2, email_3=email_3)##



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