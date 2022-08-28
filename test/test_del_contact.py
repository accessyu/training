from model.contact import Contact
from random import randrange

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname = "1",firstname="w", address="a"))
    old_contact= app.contact.get_contact_list()
    app.contact.delete_first_contact()
    app.contact.return_to_contact()
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)
    old_contact[0:1] = []
    assert sorted(old_contact) == sorted(new_contact)


def test_delete_random_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname = "1",firstname="w", address="a"))
    old_contact= app.contact.get_contact_list()
    index = randrange(len(old_contact))
    app.contact.delete_contact_by_index(index)
    app.contact.return_to_contact()
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)
    old_contact[index:index+1] = []
    assert sorted(old_contact) == sorted(new_contact)