# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys
import re

try:
    opts,args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    s= prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    return re.sub("\s+", " ",s).strip()

def random_contact():
    return Contact(firstname=random_string("name", 10), middlename=random_string("name", 20),
                      lastname=random_string("name", 10),
                      nickname="4",
                      title="11", company="12", address="23", home="44", mobile="5", work="7", fax="9",
                      email="8", bday="2", bmonth="May", byear="1", address2="1", phone2="1", notes="1")

testdata = [Contact(lastname="", firstname="", address="")] + [
   random_contact() for _ in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))

    #out.write(jsonp.dumps(testdata, default=lambda x: x.__dict__, indent=2))

