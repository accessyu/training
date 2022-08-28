class Contact:

    def __init__(self, id= None, firstname= None, middlename= None, lastname= None, nickname= None,title= None,
                 company= None,address= None,home= None,mobile= None,work= None,fax= None,email= None,
                 bday= None,bmonth= None,byear= None,address2= None,phone2= None,notes= None):
        self.id = id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes

    def __eq__(self, other):
        return ((self.id == other.id) and
        (self.lastname == other.lastname) and
        (self.firstname == other.firstname) and
        (self.address == other.address))

    def  __lt__ (self,other):
        return self.id  < other.id
    def __repr__(self):
        return '"'+", ".join([self.lastname, self.firstname, self.address]) + '"'
