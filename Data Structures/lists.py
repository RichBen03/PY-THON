# lists : ordered mutable and allows duplicate values

# Defining a list using the keyword list
names = list(("Rich", "Bill", "James", "Richard"))
print(names)

# Defining a list using square brackets
cars = ["BMV","Gle63","Aston Martin Vulcan"]
print(cars)

# Defining an empty list
empty = []
print(empty)

# Adding elements to the end of the list
empty.append("Hello")
empty.append("Zlatan")
empty.append("Ibra")
print(empty)

# Adding elements at a specific index
empty.insert(2,"Isak")
empty.insert(0,"Trent")

#Adding multiple elements to a list
empty.extend(["Pogba","Pep","Fabrizio"])


# Removing elreements from a lists
removed = names.pop()
print(names)