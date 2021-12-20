from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not len(wd.find_elements_by_name("searchstring")) > 0:
            wd.find_element_by_link_text("home").click()

    def open_add_new_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def fill_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("photo", contact.photo)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.faxphone)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_select_field_value("bday", contact.bday)
        self.change_select_field_value("bmonth", contact.bmonth)
        self.change_select_field_value("aday", contact.aday)
        self.change_select_field_value("amonth", contact.amonth)
        self.change_field_value("byear", contact.byear)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("new_group", contact.new_group)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.secondaryphone)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_select_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        self.open_add_new_page()
        # fill contact form
        self.fill_form(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_id(id).click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_css_selector("[value = 'Delete']").click()
        # accept pop-up
        wd.switch_to.alert.accept()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_css_selector("[value = 'Delete']").click()
        # accept pop-up
        wd.switch_to.alert.accept()
        self.return_to_home_page()
        self.contact_cache = None

    def move_first_contact_to_first_group(self):
        self.move_contact_by_index_to_first_group(0)

    def move_contact_by_index_to_first_group(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        # select group
        wd.find_element_by_name("to_group").click()
        Select(wd.find_element_by_name("to_group")).select_by_index("0")
        # submit add
        wd.find_element_by_name("add").click()
        self.return_to_home_page()
        self.contact_cache = None

    def open_contact_for_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        # init contact edit
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(0, contact)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_home_page()
        # init contact edit
        self.open_contact_for_edit_by_index(index)
        # edit contact
        self.fill_form(contact)
        # submit edit
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    # если такой тест не нужен, то удалить его совсем
    def open_contact_for_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        # init contact edit
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def open_contact_for_view_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        # init contact edit
        row = wd.find_elements_by_name("entry")[id]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def view_fist_contact(self):
        self.view_contact_by_index(0)

    def view_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        # view contact
        self.open_contact_for_view_by_index(index)
        self.return_to_home_page()
        self.contact_cache = None

    def view_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        # view contact
        self.open_contact_for_view_by_id(id)
        self.return_to_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector('tr')[1:]:
                cells = element.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                lastname = cells[1].text.strip()
                firstname = cells[2].text.strip()
                address = cells[3].text.strip()
                all_emails = cells[4].text.strip()
                all_phones = cells[5].text.strip()
                self.contact_cache.append(Contact(id=id, lastname=lastname, firstname=firstname, address=address,
                                                  all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_for_edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").text.strip()
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(id=id, lastname=lastname, firstname=firstname, address=address,
                       email=email, email2=email2, email3=email3,
                       homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_for_view_by_index(index)
        card_text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", card_text).group(1)
        mobilephone = re.search("M: (.*)", card_text).group(1)
        workphone = re.search("W: (.*)", card_text).group(1)
        secondatyphone = re.search("P: (.*)", card_text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondatyphone)
