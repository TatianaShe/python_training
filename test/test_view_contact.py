# -*- coding: utf-8 -*-


def test_view_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.view_first_contact()
    app.session.logout()
