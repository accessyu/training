# -*- coding: utf-8 -*-
import pytest
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
        app.open_home_page()
        app.login(username="admin",password="secret")
        app.open_groups_page()
        app.create_group(name="123", header="123", footer="123")
        app.logout()

def test_add_empty_group(app):
        app.open_home_page()
        app.login(username="admin", password="secret")
        app.open_groups_page()
        app.create_group(name="", header="", footer="")
        app.logout()
