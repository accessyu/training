# -*- coding: utf-8 -*-
from model.group import Group

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="123", header="1", footer="5"))
    app.session.logout()

def test_add_empty_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

