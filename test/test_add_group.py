# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="First Group", header="Leader of First Group", footer="Footer of First Group"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
