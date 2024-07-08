class Employee:
    def __init__(self,name,last):
        self.firstname = name
        self.lastname = last
        # self.mail = name + last + '@gmail.com'

    
    @property
    def mail(self):
        return '{}.{}@gmail.com'.format(self.firstname,self.lastname)

    @property                             #getter method
    def fullname(self):
        return '{} {}'.format(self.firstname,self.lastname)

    @fullname.setter                      #setter method
    def fullname(self,name):
        first,last = name.split()
        self.firstname = first
        self.lastname = last


e = Employee("Vaidehi", "Jadhav")
e.fullname = "Vrunda Jadhav"

print(e.firstname)
print(e.mail)
print(e.fullname)