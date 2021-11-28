# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_edit_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Alex", middlename="Sergeevich", lastname="Buth", nickname="alexalex", company="VK",
                    address="Moscow, Novaya st., 36 - 94",
                    mobilephone="89204567893", email="alex@pochta.ru", bday="17", bmonth="December", byear="1991"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Alexander", middlename="Sergeevich", lastname="Pushkin", nickname="poet", company="",
                address="St. Petersburg, Nevsky av.",
                mobilephone="", email="", bday="6", bmonth="June", byear="1799")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
