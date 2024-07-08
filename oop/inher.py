class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def showDetails(self):
        print(f"The name of employee is {self.name} and id is {self.id}")


class Programmer(Employee):
    def showLanguage(self):
        print(f"The {self.name} knows python")


e = Employee("vaidehi", 1)
e.showDetails()
e1 = Programmer("Ray", 2)
e1.showDetails()
e1.showLanguage()