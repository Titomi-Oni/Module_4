class Dog:
    # Class variable
    animal = "Dog"

    def __init__(self, breed, colour):
        # Instance variables
        self.breed = breed
        self.colour = colour

# Creating two objects
dog1 = Dog("German Shepherd", "Brown")
dog2 = Dog("Labrador", "Black")

# Displaying details
print("Dog 1:")
print("Animal:", Dog.animal)
print("Breed:", dog1.breed)
print("Colour:", dog1.colour)

print("\nDog 2:")
print("Animal:", Dog.animal)
print("Breed:", dog2.breed)
print("Colour:", dog2.colour)
