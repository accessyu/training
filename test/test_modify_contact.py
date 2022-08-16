from model.contact import Contact

def test_modify_contact_name(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(lastname = "q",firstname="w", address="a")
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts) == sorted(new_contacts)


