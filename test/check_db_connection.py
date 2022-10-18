import pymysql.cursors
import mysql.connector
from fixture.orm import ORMFixture
from model.group import Group
from fixture.db import DbFixture

#connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    groups = db.get_group_list()
    print(groups)
    contacts = db.get_contact_list()
    print(contacts)
    l = db.get_contacts_in_group(Group(id="9"))
    for item in l:
        print(item)
   # print(len(l))
    #cursor = connection.cursor()
    #cursor.execute("select * from group_list")
    #for row in cursor.fetchall():
        #print(row)
finally:
    #connection.close()
    db.destroy()
