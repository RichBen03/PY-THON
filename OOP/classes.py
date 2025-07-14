class Person:
    # A class attribute
    species="Homo Sapiens"

    # A constructor used to intialize attributes of the class
    # name and gender are parameters
    def __init__(self,name,gender):
        # Instance attributes
        self.name=name
        self.gender=gender
    # a method to return a string representation of the object
    def __str__(self):
        return f"{self.name} is a {self.gender}"
    def __del__(self):
        return f"Deleting {self.name} from memory"
    
# Creating an object which is the instance of the class
# Init function is intialized and the attributes are initialized
person1 = Person("Rich", "Male")
print(person1) # Automatically calls the str method to return the string representation of the object


# Accessing the attributes 
print(person1.name) #instance attribute
print(person1.gender)#instance attribute
print(person1.species)#class attribute

# Modifying attributes
print("\n")
print(f"The initial value for the person name was {person1.name}")
person1.name = "Max"
print(f"After modification the name was changed to {person1.name}")

del person1

print(person1)
        
        