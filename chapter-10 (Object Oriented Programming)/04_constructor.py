class Employee:
    language = "python" #this is class atrribute
    salary = 1200000

    def __init__(self, name, salary, language):   #dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("i am creating an object")


    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")


joi = Employee("Joi", 1300000, "JavaScript")
# joi.name = "Joi"
print(joi.name, joi.salary, joi.language)