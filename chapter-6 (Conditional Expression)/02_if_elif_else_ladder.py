a = int(input("Enter your age: "))

if(a>18):
    print("You are above the age of consent")

elif(a<0):
    print("Invalid negative age")

elif(a==0):
    print("Invalid zero age")
    
else:
    print("You are below the age of consent")
     