# -*- coding: utf-8 -*-
import random
from model.group import Group
from model.contact import Contact


def test_move_contact_to_group(app, db, orm):
    contact = Contact(firstname="Alexander", middlename="Sergeeevich", lastname="Pushkin", nickname="poet", title="Title1",
                    company="Poet Union", address="Boldino, Central st., 1 -15", homephone="+31278963215", mobilephone="8(921)4567893", workphone="84958963214",
                    faxphone="89994445566", email="pushkin@pochta.com", email2="pushkin2@pochta.com", email3="pushkin3@pochta.com",
                    homepage="http://www.pushkin.com", bday="6", bmonth="June", byear="1799",
                    aday="21", amonth="July", ayear="1820", address2="Moscow, Goncharova st., 8 - 77", secondaryphone="89996132578")
    if len(orm.get_contact_list()) == 0:
        app.contact.create(contact)
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="123", header="123", footer="123"))
    id_contacts_not_in_group = [i.id for i in db.get_all_contacts_not_in_groups()]
    if len(id_contacts_not_in_group) == 0:
        app.contact.create(contact)
        id_contacts_not_in_group = [i.id for i in db.get_all_contacts_not_in_groups()]
    groups = orm.get_group_list()
    contact_index = random.choice(id_contacts_not_in_group)
    group_index = random.randrange(len(groups))
    group_for_add = groups[group_index].name
    app.contact.add_contact_to_group_by_index(contact_index, group_for_add)
    new_contacts_in_group = orm.get_contact_in_group(Group(id=groups[group_index].id))
    assert str(contact_index) in str(new_contacts_in_group)


def test_remove_contact_from_group(app, db, orm):
    contact = Contact(firstname="Alexander", middlename="Sergeeevich", lastname="Pushkin", nickname="poet", title="Title1",
                    company="Poet Union", address="Boldino, Central st., 1 -15", homephone="+31278963215", mobilephone="8(921)4567893", workphone="84958963214",
                    faxphone="89994445566", email="pushkin@pochta.com", email2="pushkin2@pochta.com", email3="pushkin3@pochta.com",
                    homepage="http://www.pushkin.com", bday="6", bmonth="June", byear="1799",
                    aday="21", amonth="July", ayear="1820", address2="Moscow, Goncharova st., 8 - 77", secondaryphone="89996132578")
    if len(orm.get_contact_list()) == 0:
        app.contact.create(contact)
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="123", header="123", footer="123"))
    groups = orm.get_group_list()
    group_index = random.randrange(len(groups))
    old_group_contacts = orm.get_contact_in_group(Group(id=groups[group_index].id))
    if len(old_group_contacts) == 0:
        free_contacts = orm.get_contact_not_in_group(Group(id=groups[group_index].id))
        if len(free_contacts) == 0:
            app.contact.create()
            free_contacts = orm.get_contact_not_in_group(Group(id=groups[group_index].id))
            free_contact = free_contacts[0].id
            app.contact.add_contact_to_group_by_index(free_contact, groups[group_index].name)
            old_group_contacts = orm.get_contact_in_group(Group(id=groups[group_index].id))
        else:
            free_contact = free_contacts[random.randrange(len(free_contacts))].id
            app.contact.add_contact_to_group_by_index(free_contact, groups[group_index].name)
            old_group_contacts = orm.get_contact_in_group(Group(id=groups[group_index].id))
    contact_index = random.choice([c.id for c in old_group_contacts])
    app.contact.delete_contact_from_group_by_index(contact_index, groups[group_index].name)
    new_contacts = orm.get_contact_in_group(Group(id=groups[group_index].id))
    assert str(contact_index) not in str(new_contacts)
