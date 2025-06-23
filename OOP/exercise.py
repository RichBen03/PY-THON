# # Exercise 1: Creating a Student Class

# Instructions:

# Define a Student class with attributes like name and age. Include a method to display student information.

class Student:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"THE STUDENT'S INFORMATION IS AS FOLLOWS: The name is {self.name} and he is {self.age} years old")
        
rich = Student("rich", 21)
print(rich.display_info())

        