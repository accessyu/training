import pymysql.cursors
import mysql.connector
from fixture.orm import ORMFixture
from model.group import Group

#connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    #groups = db.get_group_list()
    l = db.get_contacts_not_in_group(Group(id="11"))
    for item in l:
        print(item)
    print(len(l))
    #cursor = connection.cursor()
    #cursor.execute("select * from group_list")
    #for row in cursor.fetchall():
        #print(row)
finally:
    #connection.close()
    pass #db.destroy()
