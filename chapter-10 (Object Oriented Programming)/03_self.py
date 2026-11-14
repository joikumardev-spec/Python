class Employee:
    language = "python" #this is class atrribute
    salary = 1200000


    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")


joi = Employee()
joi.language = "Java Script" #this is instance attribute
joi.greet()
joi.getinfo()