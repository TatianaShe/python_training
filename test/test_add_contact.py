# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for _ in range(random.randrange(maxlen))])

quantity_tests_for_parameter = 1

test_data = [Contact(firstname="Nikolay", middlename="Vassilievich", lastname="Gogol", nickname="writer", title="Title",
                    company="Writer Union", address="Dikanka, 8 - 13", homephone="+31278963215", mobilephone="8(921)4567893", workphone="84958963214",
                    faxphone="89994445566", email="gogol@pochta.com", email2="gogol2@pochta.com", email3="gogol3@pochta.com",
                    homepage="http://www.gogol.com", bday="1", bmonth="April", byear="1809",
                    aday="21", amonth="July", ayear="1829", address2="Moscow, Night st., 8 - 77", secondaryphone="89996132578")] + \
            [Contact(firstname=random_string("firstname", 20), middlename="Vassilievich", lastname="Gogol", nickname="writer", title="Title",
                    company="Writer Union", address="Dikanka, 8 - 13", homephone="+31278963215", mobilephone="8(921)4567893", workphone="84958963214",
                    faxphone="89994445566", email="gogol@pochta.com", email2="gogol2@pochta.com", email3="gogol3@pochta.com",
                    homepage="http://www.gogol.com", bday="1", bmonth="April", byear="1809",
                    aday="21", amonth="July", ayear="1829", address2="Moscow, Night st., 8 - 77", secondaryphone="89996132578")
             for _ in range(quantity_tests_for_parameter)] + \
            [Contact(firstname="Nikolay", middlename=random_string("middlename", 20), lastname="Gogol", nickname="writer", title="Title",
                    company="Writer Union", address="Dikanka, 8 - 13", homephone="+31278963215", mobilephone="8(921)4567893", workphone="84958963214",
                    faxphone="89994445566", email="gogol@pochta.com", email2="gogol2@pochta.com", email3="gogol3@pochta.com",
                    homepage="http://www.gogol.com", bday="1", bmonth="April", byear="1809",
                    aday="21", amonth="July", ayear="1829", address2="Moscow, Night st., 8 - 77", secondaryphone="89996132578")
             for _ in range(quantity_tests_for_parameter)] + \
            [Contact(firstname="Nikolay", middlename="Vassilievich", lastname=random_string("lastname", 30), nickname="writer", title="Title",
                    company="Writer Union", address="Dikanka, 8 - 13", homephone="+31278963215", mobilephone="8(921)4567893", workphone="84958963214",
                    faxphone="89994445566", email="gogol@pochta.com", email2="gogol2@pochta.com", email3="gogol3@pochta.com",
                    homepage="http://www.gogol.com", bday="1", bmonth="April", byear="1809",
                    aday="21", amonth="July", ayear="1829", address2="Moscow, Night st., 8 - 77", secondaryphone="89996132578")
             for _ in range(quantity_tests_for_parameter)] + \
            [Contact(firstname="Nikolay", middlename="Vassilievich", lastname="Gogol", nickname=random_string("nickname", 20), title="Title",
                    company="Writer Union", address="Dikanka, 8 - 13", homephone="+31278963215", mobilephone="8(921)4567893", workphone="84958963214",
                    faxphone="89994445566", email="gogol@pochta.com", email2="gogol2@pochta.com", email3="gogol3@pochta.com",
                    homepage="http://www.gogol.com", bday="1", bmonth="April", byear="1809",
                    aday="21", amonth="July", ayear="1829", address2="Moscow, Night st., 8 - 77", secondaryphone="89996132578")
             for _ in range(quantity_tests_for_parameter)] + \
            [Contact(firstname="Nikolay", middlename="Vassilievich", lastname="Gogol", nickname="writer", title=random_string("title", 20),
                    company="Writer Union", address="Dikanka, 8 - 13", homephone="+31278963215", mobilephone="8(921)4567893", workphone="84958963214",
                    faxphone="89994445566", email="gogol@pochta.com", email2="gogol2@pochta.com", email3="gogol3@pochta.com",
                    homepage="http://www.gogol.com", bday="1", bmonth="April", byear="1809",
                    aday="21", amonth="July", ayear="1829", address2="Moscow, Night st., 8 - 77", secondaryphone="89996132578")
             for _ in range(quantity_tests_for_parameter)] + \
            [Contact(firstname="Nikolay", middlename="Vassilievich", lastname="Gogol", nickname="writer", title="Title",
                    company=random_string("company", 30), address="Dikanka, 8 - 13", homephone="+31278963215", mobilephone="8(921)4567893", workphone="84958963214",
                    faxphone="89994445566", email="gogol@pochta.com", email2="gogol2@pochta.com", email3="gogol3@pochta.com",
                    homepage="http://www.gogol.com", bday="1", bmonth="April", byear="1809",
                    aday="21", amonth="July", ayear="1829", address2="Moscow, Night st., 8 - 77", secondaryphone="89996132578")
             for _ in range(quantity_tests_for_parameter)] + \
            [Contact(firstname="Nikolay", middlename="Vassilievich", lastname="Gogol", nickname="writer", title="Title",
                    company="Writer Union", address=random_string("address", 50), homephone="+31278963215", mobilephone="8(921)4567893", workphone="84958963214",
                    faxphone="89994445566", email="gogol@pochta.com", email2="gogol2@pochta.com", email3="gogol3@pochta.com",
                    homepage="http://www.gogol.com", bday="1", bmonth="April", byear="1809",
                    aday="21", amonth="July", ayear="1829", address2="Moscow, Night st., 8 - 77", secondaryphone="89996132578")
             for _ in range(quantity_tests_for_parameter)] + \
            [Contact(firstname="Nikolay", middlename="Vassilievich", lastname="Gogol", nickname="writer", title="Title",
                    company="Writer Union", address="Dikanka, 8 - 13", homephone=random_string("homephone", 20), mobilephone="8(921)4567893", workphone="84958963214",
                    faxphone="89994445566", email="gogol@pochta.com", email2="gogol2@pochta.com", email3="gogol3@pochta.com",
                    homepage="http://www.gogol.com", bday="1", bmonth="April", byear="1809",
                    aday="21", amonth="July", ayear="1829", address2="Moscow, Night st., 8 - 77", secondaryphone="89996132578")
             for _ in range(quantity_tests_for_parameter)] + \
            [Contact(firstname="Nikolay", middlename="Vassilievich", lastname="Gogol", nickname="writer", title="Title",
                    company="Writer Union", address="Dikanka, 8 - 13", homephone="+31278963215", mobilephone=random_string("mobilephone", 20), workphone="84958963214",
                    faxphone="89994445566", email="gogol@pochta.com", email2="gogol2@pochta.com", email3="gogol3@pochta.com",
                    homepage="http://www.gogol.com", bday="1", bmonth="April", byear="1809",
                    aday="21", amonth="July", ayear="1829", address2="Moscow, Night st., 8 - 77", secondaryphone="89996132578")
             for _ in range(quantity_tests_for_parameter)] + \
            [Contact(firstname="Nikolay", middlename="Vassilievich", lastname="Gogol", nickname="writer", title="Title",
                    company="Writer Union", address="Dikanka, 8 - 13", homephone="+31278963215", mobilephone="8(921)4567893", workphone=random_string("workphone", 20),
                    faxphone="89994445566", email="gogol@pochta.com", email2="gogol2@pochta.com", email3="gogol3@pochta.com",
                    homepage="http://www.gogol.com", bday="1", bmonth="April", byear="1809",
                    aday="21", amonth="July", ayear="1829", address2="Moscow, Night st., 8 - 77", secondaryphone="89996132578")
             for _ in range(quantity_tests_for_parameter)] + \
            [Contact(firstname="Nikolay", middlename="Vassilievich", lastname="Gogol", nickname="writer", title="Title",
                    company="Writer Union", address="Dikanka, 8 - 13", homephone="+31278963215", mobilephone="8(921)4567893", workphone="84958963214",
                    faxphone=random_string("faxphone", 20), email="gogol@pochta.com", email2="gogol2@pochta.com", email3="gogol3@pochta.com",
                    homepage="http://www.gogol.com", bday="1", bmonth="April", byear="1809",
                    aday="21", amonth="July", ayear="1829", address2="Moscow, Night st., 8 - 77", secondaryphone="89996132578")
             for _ in range(quantity_tests_for_parameter)] + \
            [Contact(firstname="Nikolay", middlename="Vassilievich", lastname="Gogol", nickname="writer", title="Title",
                    company="Writer Union", address="Dikanka, 8 - 13", homephone="+31278963215", mobilephone="8(921)4567893", workphone="84958963214",
                    faxphone="89994445566", email=random_string("email", 30), email2="gogol2@pochta.com", email3="gogol3@pochta.com",
                    homepage="http://www.gogol.com", bday="1", bmonth="April", byear="1809",
                    aday="21", amonth="July", ayear="1829", address2="Moscow, Night st., 8 - 77", secondaryphone="89996132578")
             for _ in range(quantity_tests_for_parameter)] + \
            [Contact(firstname="Nikolay", middlename="Vassilievich", lastname="Gogol", nickname="writer", title="Title",
                    company="Writer Union", address="Dikanka, 8 - 13", homephone="+31278963215", mobilephone="8(921)4567893", workphone="84958963214",
                    faxphone="89994445566", email="gogol@pochta.com", email2=random_string("email2", 30), email3="gogol3@pochta.com",
                    homepage="http://www.gogol.com", bday="1", bmonth="April", byear="1809",
                    aday="21", amonth="July", ayear="1829", address2="Moscow, Night st., 8 - 77", secondaryphone="89996132578")
             for _ in range(quantity_tests_for_parameter)] + \
            [Contact(firstname="Nikolay", middlename="Vassilievich", lastname="Gogol", nickname="writer", title="Title",
                    company="Writer Union", address="Dikanka, 8 - 13", homephone="+31278963215", mobilephone="8(921)4567893", workphone="84958963214",
                    faxphone="89994445566", email="gogol@pochta.com", email2="gogol2@pochta.com", email3=random_string("email3", 30),
                    homepage="http://www.gogol.com", bday="1", bmonth="April", byear="1809",
                    aday="21", amonth="July", ayear="1829", address2="Moscow, Night st., 8 - 77", secondaryphone="89996132578")
             for _ in range(quantity_tests_for_parameter)] + \
            [Contact(firstname="Nikolay", middlename="Vassilievich", lastname="Gogol", nickname="writer", title="Title",
                    company="Writer Union", address="Dikanka, 8 - 13", homephone="+31278963215", mobilephone="8(921)4567893", workphone="84958963214",
                    faxphone="89994445566", email="gogol@pochta.com", email2="gogol2@pochta.com", email3="gogol3@pochta.com",
                    homepage=random_string("homepage", 30), bday="1", bmonth="April", byear="1809",
                    aday="21", amonth="July", ayear="1829", address2="Moscow, Night st., 8 - 77", secondaryphone="89996132578")
             for _ in range(quantity_tests_for_parameter)] + \
            [Contact(firstname="Nikolay", middlename="Vassilievich", lastname="Gogol", nickname="writer", title="Title",
                    company="Writer Union", address="Dikanka, 8 - 13", homephone="+31278963215", mobilephone="8(921)4567893", workphone="84958963214",
                    faxphone="89994445566", email="gogol@pochta.com", email2="gogol2@pochta.com", email3="gogol3@pochta.com",
                    homepage="http://www.gogol.com", bday="1", bmonth="April", byear="1809",
                    aday="21", amonth="July", ayear="1829", address2=random_string("address", 30), secondaryphone="89996132578")
             for _ in range(quantity_tests_for_parameter)] + \
            [Contact(firstname="Nikolay", middlename="Vassilievich", lastname="Gogol", nickname="writer", title="Title",
                    company="Writer Union", address="Dikanka, 8 - 13", homephone="+31278963215", mobilephone="8(921)4567893", workphone="84958963214",
                    faxphone="89994445566", email="gogol@pochta.com", email2="gogol2@pochta.com", email3="gogol3@pochta.com",
                    homepage="http://www.gogol.com", bday="1", bmonth="April", byear="1809",
                    aday="21", amonth="July", ayear="1829", address2="Moscow, Night st., 8 - 77", secondaryphone=random_string("secondaryphone", 20))
             for _ in range(quantity_tests_for_parameter)]

    
@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
