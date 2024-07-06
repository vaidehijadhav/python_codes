## Parameterized Constructor
# class Details:
#     def __init__(self, name, occupation):
#         self.name = name
#         self.occupation = occupation
    
#     def display(self):
#         print(f"{self.name} is {self.occupation}")

# obj1 = Details("Ray", "Software Engineer")
# obj1.display()

## Default Constructor
class Details:
    def __init__(self):
        self.name = "Ray"
        self.occupation = "Software Engineer"
        print(f"{self.name} is {self.occupation}")

obj1 = Details()