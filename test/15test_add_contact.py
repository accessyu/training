# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string
import re

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    s= prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    return re.sub("\s+", " ",s).strip()

def random_contact():
    return Contact(firstname=random_string("name", 10), middlename=random_string("name", 20),
                      lastname=random_string("name", 10),
                      nickname="4",
                      title="11", company="12", address="23", home="44", mobile="5", work="7", fax="9",
                      email="8", bday="2", bmonth="May", byear="1", address2="1", phone2="1", notes="1")

testdata = [Contact(lastname="", firstname="",address="")] + [
   random_contact() for _ in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
        old_contacts = app.contact.get_contact_list()

        app.contact.create(contact)
        app.contact.return_to_contact()
        assert len(old_contacts) + 1 == app.contact.count
        new_contacts = app.contact.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts) == sorted(new_contacts)