import re

def test_phones_on_home_page(app, db):
    contacts1 = app.contact.get_contact_list()
    contacts2 = db.get_contact_list()
    assert len(contacts1) == len(contacts2)
    contacts1.sort()
    contacts2.sort()
    for i in range(len(contacts1)):
        assert contacts1[i].id == contacts2[i].id
        assert clear(contacts1[i].firstname) == clear(contacts2[i].firstname)
        assert clear(contacts1[i].lastname) == clear(contacts2[i].lastname)

def clear(s):
    return re.sub("\s\s*" , " ", s.strip())
