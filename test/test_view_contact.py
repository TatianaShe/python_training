# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_view_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Alex", middlename="Sergeevich", lastname="Buth", nickname="alexalex", company="VK",
                    address="Moscow, Novaya st., 36 - 94",
                    mobilephone="89204567893", email="alex@pochta.ru", bday="17", bmonth="December", byear="1991"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.view_contact_by_index(index)
    # проверяем, что количество контактов не изменилось
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    # проверяем, что контакт, карточку которого смотрели, остался на своем месте
    assert new_contacts[index].id == old_contacts[index].id
