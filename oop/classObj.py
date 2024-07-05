class Person:
    name = "Ray"
    age = 21
    occupation = "Software Engineer"

    def  info(self):
        print(f"This is {self.name} and He is {self.occupation}")


obj1 = Person()

obj1.name = "Vaidehi"
obj1.age = 22


print(obj1.name)
# print(obj1.info())      # Output-->none
obj1.info()
