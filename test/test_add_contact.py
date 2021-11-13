# -*- coding: utf-8 -*-
from model.contact import Contact

    
def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Sergey", middlename="Petrovich", lastname="Ivanov", nickname="drummer", company="Mail", address="Moscow, Lenina st., 3 - 9",
                               mobile="89111234567", email="ivanov@pochta.ru", bday="4", bmonth="May", byear="1980"))
    app.session.logout()

def test_add_contact_with_empty_middlename(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Anton", middlename="", lastname="Suvorov", nickname="tonton", company="Lenta", address="Tula, Pravdy st., 8 - 12",
                               mobile="89214567896", email="tonton@pochta.ru", bday="21", bmonth="July", byear="1994"))
    app.session.logout()
