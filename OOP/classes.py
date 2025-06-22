class Dog:
    # intializes the class variable
    species = "German Shephard"

    # intializing the object attributes
    # self parameter references the current instance
    def __init__(self, name,age):

        # intializing the instance variable
        self.name = name
        self.age = age

# Creating objects, the objects have attributes
dog1 = Dog("Maddy", 2)
dog2 = Dog("Ken", 3)

print(dog1.name, dog1.age)
print(dog2.name,dog2.age)

# Modifying the instance variable
print("Changing dog1's name",end="\n")
dog1.name = "bill"
print(dog1.name)

# Modifying the class variable
Dog.species= "Wolf"
print("Class variable is", Dog.species)
print(dog1.species)
print(dog2.species)

