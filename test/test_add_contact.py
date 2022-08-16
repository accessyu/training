# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
        old_contacts = app.contact.get_contact_list()
        contact = Contact(firstname="1", middlename="2", lastname="3", nickname="4",
                                   title="11",company="12",address="23",home="44",mobile="5",work="7",fax="9",
                                   email="8",bday="2",bmonth="May",byear="1",address2="1",phone2="1",notes="1")
        #app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="",#
                                   #title="",company="",address="",home="",mobile="",work="",fax="",#
                                   #email="",bday="2",bmonth="May",byear="",address2="",phone2="",notes=""))#
        app.contact.create(contact)
        app.contact.return_to_contact()
        assert len(old_contacts) + 1 == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts) == sorted(new_contacts)





