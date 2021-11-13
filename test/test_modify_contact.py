# -*- coding: utf-8 -*-
from model.contact import AddToGroup


def test_add_first_contact_to_group(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_first_contact_to_group(AddToGroup(to_group="Group for Add"))
    app.session.logout()
