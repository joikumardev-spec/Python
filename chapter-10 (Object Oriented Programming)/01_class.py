class Employee:
    language = "python" #this is class atrribute
    salary = 1200000


joi = Employee()
joi.name = "Joi" #this is instance attribute
print(joi.name, joi.language, joi.salary)

rohan = Employee()
rohan.name = "Rohan"
print(rohan.name, rohan.salary, rohan.language)


# here name is instance attribute and salary and language
# are class attributes as they directly belong
# to the class