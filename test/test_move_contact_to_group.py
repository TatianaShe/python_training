# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group


def test_move_first_contact_to_first_group(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Alex", middlename="Sergeevich", lastname="Buth", nickname="alexalex", company="VK",
                    address="Moscow, Novaya st., 36 - 94",
                    mobilephone="89204567893", email="alex@pochta.ru", bday="17", bmonth="December", byear="1991"))
    if app.group.count() == 0:
        app.group.create(Group(name="Group for contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.move_first_contact_to_first_group()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
