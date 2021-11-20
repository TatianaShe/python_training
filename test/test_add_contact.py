# -*- coding: utf-8 -*-
from model.contact import Contact

    
def test_add_contact(app):
    app.contact.create(Contact(firstname="Sergey", middlename="Petrovich", lastname="Ivanov", nickname="drummer", company="Mail", address="Moscow, Lenina st., 3 - 9",
                               mobilephone="89111234567", email="ivanov@pochta.ru", bday="4", bmonth="May", byear="1980"))

def test_add_contact_with_empty_middlename(app):
    app.contact.create(Contact(firstname="Anton", lastname="Suvorov", nickname="tonton", company="Lenta", address="Tula, Pravdy st., 8 - 12",
                               mobilephone="89214567896", email="tonton@pochta.ru", bday="21", bmonth="July", byear="1994"))
