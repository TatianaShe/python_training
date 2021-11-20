# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Alex", middlename="Sergeevich", lastname="Buth", nickname="alexalex", company="VK",
                    address="Moscow, Novaya st., 36 - 94",
                    mobilephone="89204567893", email="alex@pochta.ru", bday="17", bmonth="December", byear="1991"))
    app.contact.edit_first_contact(
        Contact(firstname="Alexander", middlename="Sergeevich", lastname="Pushkin", nickname="poet", company="",
                address="St. Petersburg, Nevsky av.",
                mobilephone="", email="", bday="6", bmonth="June", byear="1799"))
