from model.contact import Contact
import random

def test_edit_contact_name(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test"))
    old_contact_list = db.get_contact_list()
    contact = random.choice(old_contact_list)
    new_data = Contact(firstname="Changed", lastname="VALUE")
    app.contact.edit_by_id(contact.id, new_data)
    new_contact_list = db.get_contact_list()
    for item in old_contact_list:
        if item.id == contact.id:
            item.firstname = new_data.firstname
            item.lastname = new_data.lastname
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
