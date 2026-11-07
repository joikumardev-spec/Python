marks = {
    "abc": 100,
    "dce": 50,
    "efg": 80,
    0:"xyz"
}
print(marks.items())  # prints key values (everything in dict)

print(marks.keys()) #prints keys of dict (abc , dce, efg,0)

print(marks.value()) # prints values of dict (11 , 50 , 80 , xyz)


marks.update({"abc": 99}) # changes marks of abc from 100 to 99

marks.update({"jhk":88}) # adds key value to dict is not already present

print(marks.get("abc")) #prints marks of abc
print(marks["abc"]) #gives same value 

#but when the key is not in dict:

print(marks.get("harry")) #prints none
print(marks["harry"]) #Returns an error
