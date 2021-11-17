# -*- coding: utf-8 -*-


def test_move_first_contact_to_first_group(app):
    app.session.login(username="admin", password="secret")
    app.contact.move_first_contact_to_first_group()
    app.session.logout()
