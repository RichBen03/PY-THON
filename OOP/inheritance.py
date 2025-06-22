class Dog:
    def __init__(self,name):
        self.name= name

    def display(self):
        print(f"The dog's name is {self.name}")

# Single inheritance which inherits from the class Dog
class Labrador(Dog):
    def sound(self):
        print("Labrador barks")

# Initiliazing multilevel inheritance where a child class inherits from a parent class which then inherits from a another class
class GuideDog(Labrador):
    def guide(self):
        print(f"{self.name} Guides the way")
class German:
    def greet(self):
        print('German Dog says Hello')

# Initializing the multiple inheritance where Germany inherits from German and Dog classes
class Germany(German,Dog):
    def sound(self):
        print("German Dog barks")

lab = Labrador("Billy")
lab.display()
lab.sound()

guider = GuideDog("Njoro")
guider.display()
guider.sound()
guider.guide()

germans = Germany("Maxy")
germans.display()
germans.greet()
germans.sound()
    
# Single Inheritance = labrador inherits from Dog class
# Mulitilevel Inheritance = GuideDog inherits from Labrador where Labrador inherits from dog
# Multiple Inheritance = German inherits from Germany and Dog classes
        