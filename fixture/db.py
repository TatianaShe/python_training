import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list")
            for row in cursor:
                (id, name, header, footer) = row
                group_list.append(Group(name=name, header=header, footer=footer, id=str(id)))
        finally:
            cursor.close()
        return group_list

    def get_contact_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("""SELECT id, firstname, middlename, lastname, nickname, company, title, address, home, 
            mobile, work, fax, email, email2, email3, homepage, 
            bday, bmonth, byear, aday, amonth, ayear, address2, phone2 
            FROM addressbook 
            WHERE deprecated ='0000-00-00 00:00:00'""")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company,
                 title, address, homephone, mobilephone, workphone, faxphone, email, email2,
                 email3, homepage, bday, bmonth, byear, aday, amonth,
                 ayear, address2, secondaryphone) = row
                contact_list.append(Contact(id=str(id), firstname=firstname, middlename=middlename,
                                            lastname=lastname, nickname=nickname,
                                            title=title, company=company,
                                            address=address, homephone=homephone,
                                            mobilephone=mobilephone, workphone=workphone,
                                            faxphone=faxphone, email=email,
                                            email2=email2, email3=email3,
                                            homepage=homepage,
                                            bday=bday, bmonth=bmonth, byear=byear,
                                            aday=aday, amonth=amonth, ayear=ayear,
                                            address2=address2, secondaryphone=secondaryphone))
        finally:
            cursor.close()
        return contact_list

    def destroy(self):
        self.connection.close()
