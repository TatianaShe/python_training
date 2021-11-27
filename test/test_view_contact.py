# -*- coding: utf-8 -*-
from model.contact import Contact


def test_view_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Alex", middlename="Sergeevich", lastname="Buth", nickname="alexalex", company="VK",
                    address="Moscow, Novaya st., 36 - 94",
                    mobilephone="89204567893", email="alex@pochta.ru", bday="17", bmonth="December", byear="1991"))
    old_contacts = app.contact.get_contact_list()
    app.contact.view_first_contact()
    # проверяем, что количество контактов не изменилось
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    # проверяем, что первый контакт, карточку которого смотрели (первый), остался на своем месте
    assert new_contacts[0].id == old_contacts[0].id
