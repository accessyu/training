# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
        app.open_home_page()
        app.session.login(username="admin",password="secret")
        app.open_contact_page()
        app.create_contact(Contact(firstname="", middlename="", lastname="", nickname="",
                                   title="",company="",address="",home="",mobile="",work="",fax="",
                                   email="",bday="2",bmonth="May",byear="",address2="",phone2="",notes=""))
        app.session.logout()

def test_add_empty_contact(app):
        app.open_home_page()
        app.session.login(username="admin", password="secret")
        app.open_contact_page()
        app.create_contact(Contact(firstname="", middlename="", lastname="", nickname="",title="",company="",
                                   address="",home="",mobile="",work="",fax="",email="",bday="1",bmonth="May",
                                   byear="",address2="",phone2="",notes=""))
        app.session.logout()

