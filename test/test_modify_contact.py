# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(
        Contact(firstname="Alexander", middlename="Sergeevich", lastname="Pushkin", nickname="poet", company="",
                address="St. Petersburg, Nevsky av.",
                mobile="", email="", bday="6", bmonth="June", byear="1799"))
    app.session.logout()
