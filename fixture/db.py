import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=name,
                             autocommit=True #кеш во время кадого запроса будет сбрасываться
                            )


    def get_group_list(self): #загружает объекты из базы данных
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list


    def get_contact_list(self): #загружает объекты из бд
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, email, email2,"
                           " email3, phone2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, homephone, mobilephone, workphone, email, email2, email3, phone2) = row
                list.append(Contact(id=str(id), name=firstname, lastname=lastname, phone_home=homephone,
                                    mobile_home=mobilephone, phone_work=workphone, address_1=address, email_1=email,
                                    email_2=email2, email_3=email3, phone_home_2=phone2))
        finally:
            cursor.close()
        return list



    def destroy(self):
        self.connection.close()