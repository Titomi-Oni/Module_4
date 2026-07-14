#Write a Python program to create a class named Dog. 
# Create a class attribute named species with the value "Canine". 
# Use the constructor to initialize the dog's name and age.
#  Create two objects and print their species, name, and age.
class Dog:
    species = "Canine"
    
    def __init__(self,mileage, age):
        self.mileage = mileage
        self.age = age

d1 = Dog("Rocky", 2)

print (d1.mileage)
print (d1.age)