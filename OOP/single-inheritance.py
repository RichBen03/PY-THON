class Book:
    def __init__(self, title, author):
        self.title=title
        self.author=author

    def __str__(self):
        return f"The book {self.title} was written by {self.author}"
    
    def read(self):
        return f"The book {self.title} is currently being read"

# Single Inheritance- inherits the methods and attributes of class book
class TextBook(Book):
    def close(self):
        return f"The Textbook has been closed"
    
myBook = Book("Atomic Habits", "James Clear")
myTextBook =  TextBook("Primary Science 6", "KBS")
print(myBook.read())
print(myTextBook.close())
print(myTextBook.read())
    
    