# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Group for deletion", header="something", footer="anything else"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Newest Group")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
