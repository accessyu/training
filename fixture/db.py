import pymysql
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name,  user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select group_id, group_name, group_header, group_footer from group_list')
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_in_group_list(self):
        keys = ['id', 'group_id']
        pairs = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id,group_id) = row
                dictionary = dict(zip(keys, row))
                pairs.append(dictionary)
        finally:
            cursor.close()
        return pairs

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, email, email2, email3,"
                           "phone2 from addressbook where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, homephone, mobilephone, workphone, email, email2, email3, phone2) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, home_phone=homephone, cell_phone=mobilephone, work_phone=workphone,
                                    address=address, email_1=email, email_2=email2, email_3=email3, secondary_phone=phone2))
        finally:
            cursor.close()
        return list


    def destroy(self):
        self.connection.close()