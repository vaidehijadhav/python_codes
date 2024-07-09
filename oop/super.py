class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id


class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang = lang


e1 = Employee("vaidehi", 10)
e2 = Programmer("ray",11, "python")
print(e1.name)
print(e2.name)
