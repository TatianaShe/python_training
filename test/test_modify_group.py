# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group for deletion", header="something", footer="anything else"))
    app.group.modify_first_group(Group(name="Newest Group"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group for deletion", header="something", footer="anything else"))
    app.group.modify_first_group(Group(header="Newest Header"))
