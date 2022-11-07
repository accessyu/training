import re

def  test_phones_on_home_page(app, contact_from_home_page=None):
    contact_from_home_page = app.contact.get_contact_list() [0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.fax == contact_from_edit_page.fax

def test_phones_on_home_page_db(app, db):
    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    assert len(contacts_from_db) == len(contacts_from_home_page)
    contacts_from_home_page.sort(key=lambda x: x.id)
    contacts_from_db.sort(key=lambda x: x.id)
    for i in range(len(contacts_from_db)):
        assert contacts_from_home_page[i].id == contacts_from_db[i].id
        assert contacts_from_home_page[i].all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db[i])
        assert contacts_from_home_page[i].firstname == clear_space(contacts_from_db[i].firstname)
        assert contacts_from_home_page[i].lastname == clear_space(contacts_from_db[i].lastname)
        assert contacts_from_home_page[i].address == clear_crnl(contacts_from_db[i].address)
        assert contacts_from_home_page[i].all_emails_from_home_page == merge_emails_like_on_home_page(contacts_from_db[i])

def clear(s):
    return re.sub("[() -]", "", s)

def clear_crnl(s):
    return re.sub("\r\n", "\n", s)

def clear_space(s):
    return re.sub("\s+", " ", s).strip()

def clear_email(s):
    return s.strip()


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home,contact.mobile, contact.work,
                                        contact.phone2]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_email(x),
                                filter(lambda x: x is not None,
                                       [contact.email1,contact.email2,contact.email3]))))
