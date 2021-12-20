# -*- coding: utf-8 -*-
from random import randrange
from model.contact import Contact


def test_edit_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(
            Contact(firstname="Alex", middlename="Sergeevich", lastname="Buth", nickname="alexalex", company="VK",
                    address="Moscow, Novaya st., 36 - 94",
                    mobilephone="89204567893", email="alex@pochta.ru", bday="17", bmonth="December", byear="1991"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Alexander", middlename="Sergeevich", lastname="Pushkin", nickname="poet", company="",
                      address="St. Petersburg, Nevsky av.",
                      mobilephone="", email="", bday="6", bmonth="June", byear="1799")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
