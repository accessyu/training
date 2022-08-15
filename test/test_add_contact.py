# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
        app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="",
                                   title="",company="",address="",home="",mobile="",work="",fax="",
                                   email="",bday="2",bmonth="May",byear="",address2="",phone2="",notes=""))


def test_add_empty_contact(app):
        app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="",title="",company="",
                                   address="",home="",mobile="",work="",fax="",email="",bday="1",bmonth="May",
                                   byear="",address2="",phone2="",notes=""))


