import time

from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_new_page(self):
        wd = self.app.wd
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
        self.app.open_home_page()
        self.open_add_new_page()
        # fill contact form
        self.fill_form(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.app.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_css_selector("[value = 'Delete']").click()
        #accept pop-up
        wd.switch_to.alert.accept()
        self.return_to_home_page()

    def move_first_contact_to_first_group(self):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # select group
        wd.find_element_by_name("to_group").click()
        Select(wd.find_element_by_name("to_group")).select_by_index("0")
        # submit add
        wd.find_element_by_name("add").click()
        self.return_to_home_page()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # init contact edit
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # edit contact
        self.fill_form(contact)
        # submit edit
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()

    # если такой тест не нужен, то удалить его совсем
    def view_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        # view contact
        wd.find_element_by_xpath("//img[@alt='Details']").click()
        self.return_to_home_page()
        # после удаления этого оиждания в application.py тест падает
        # ругается, что не успевает разлогиниться, поэтому поставила сюда
        wd.implicitly_wait(2)

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))
