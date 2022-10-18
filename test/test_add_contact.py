# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app, data_contacts, check_ui, db):
        contact = data_contacts
        old_contacts = db.get_contact_list()
        app.contact.create(contact)
        app.contact.return_to_contact()
        #assert len(old_contacts) + 1 == app.contact.count
        new_contacts = db.get_contact_list()
        known_ids={c.id for c in new_contacts}
        new_ids = known_ids.difference(c.id for c in old_contacts)
        assert len(new_ids) == 1
        contact.id = new_ids.pop()
        old_contacts.append(contact)
        assert sorted(old_contacts) == sorted(new_contacts)





