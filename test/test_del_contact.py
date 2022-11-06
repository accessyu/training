from model.contact import Contact
from random import randrange


def test_delete_first_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    if app.contact.count == 0:
        app.contact.create(Contact(lastname = "1",firstname="w", address="a"))
        app.contact.return_to_contact()
    old_contact= db.get_contact_list()
    app.contact.delete_first_contact()
    app.contact.return_to_contact()
    new_contact = db.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)
    old_contact[0:1] = []
    if check_ui:
        assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


def test_delete_random_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    if app.contact.count == 0:
        app.contact.create(Contact(lastname = "1",firstname="w", address="a"))
        app.contact.return_to_contact()
    old_contact= db.get_contact_list()
    index = randrange(len(old_contact))
    app.contact.delete_contact_by_index(index)
    app.contact.return_to_contact()
    new_contact = db.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)
    old_contact[index:index+1] = []
    if check_ui:
        assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


