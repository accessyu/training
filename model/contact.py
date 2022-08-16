class Contact:

    def __init__(self, firstname= None, middlename= None, lastname= None, nickname= None,title= None,
                 company= None,address= None,home= None,mobile= None,work= None,fax= None,email= None,
                 bday= None,bmonth= None,byear= None,address2= None,phone2= None,notes= None):
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
        return (self.firstname == other.firstname)\
               and (self.lastname == other.lastname)\
               and (self.address == other.address)
    def  __lt__ (self,other):
        return (self.lastname,self.firstname,self.address)  < (other.lastname,other.firstname,other.address)

