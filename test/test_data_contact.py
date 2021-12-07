from model.contact import Contact
from random import randrange
import re


def test_data_contact_page(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Nikolay", middlename="Vassilievich", lastname="Gogol ", nickname="writer", title="Title",
                    company="Writer Union", address="Dikanka, 8 - 13", homephone="+31278963215", mobilephone="8(921)4567893", workphone="84958963214",
                    faxphone="89994445566", email="gogol@pochta.com", email2="gogol2@pochta.com", email3="gogol3@pochta.com",
                    homepage="http://www.gogol.com", bday="1", bmonth="April", byear="1809",
                    aday="21", amonth="July", ayear="1829", address2="Moscow, Night st., 8 - 77", secondaryphone="89996132578"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3])))
