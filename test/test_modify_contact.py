from model.contact import Contact
from random import randrange

def test_modify_contact_name(app, db, check_ui):
    if app.contact.count == 0:
        app.contact.create(Contact(lastname = "1",firstname="w", address="a"))
        app.contact.return_to_contact()
    old_contacts = db.get_contact_list()
    contact = Contact(id=old_contacts[0].id, lastname = "q",firstname="w", address="a")
    app.contact.modify_first_contact(contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_modify_random_contact(app, db, check_ui):
    if app.contact.count == 0:
        app.contact.create(Contact(lastname = "1",firstname="w", address="a"))
        app.contact.return_to_contact()
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(id=old_contacts[index].id,lastname="q", firstname="w", address="a")
    app.contact.modify_contact_by_index(index,contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

