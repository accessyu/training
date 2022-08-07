# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.open_home_page()
    app.group.create(Group(name="123", header="1", footer="5"))

def test_add_empty_group(app):
    app.open_home_page()
    app.group.create(Group(name="", header="", footer=""))

