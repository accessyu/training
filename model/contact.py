class Contact:

    def __init__(self, id= None, all_emails_from_home_page=None,
                 firstname= "", middlename= None, lastname= "", nickname= None,title= None,
                 company= None,address= "",home= None,mobile= None,work= None,fax= None,email1 = None,email2 = None,
                 email3 =None,bday= None,bmonth= None,byear= None,address2= None,phone2= None,notes= None, all_phones_from_home_page=None):
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
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __eq__(self, other):
        return ((self.id == other.id) and
        (self.lastname == other.lastname) and
        (self.firstname == other.firstname) and
        (self.address == other.address))


    def  __lt__ (self,other):
        return self.id  < other.id
    def __repr__(self):
        return '"'+", ".join([self.lastname, self.firstname, self.address]) + '"'
