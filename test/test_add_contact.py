# -*- coding: utf-8 -*-
from model.contact import Contact

    
def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Sergey", middlename="Petrovich", lastname="Ivanov", nickname="drummer", company="Mail", address="Moscow, Lenina st., 3 - 9",
                               mobilephone="89111234567", email="ivanov@pochta.ru", bday="4", bmonth="May", byear="1980")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_add_contact_with_empty_middlename(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Anton", lastname="Suvorov", nickname="tonton", company="Lenta", address="Tula, Pravdy st., 8 - 12",
                               mobilephone="89214567896", email="tonton@pochta.ru", bday="21", bmonth="July", byear="1994")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
