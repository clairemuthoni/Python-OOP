class Book:
    def __init__(self, title, author, total_copies):
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def borrow_book(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False
    
    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
        
    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.available_copies}/{self.total_copies} available)"
    

class Library:
    def __init__(self):
        self.books = {}
    
    def add_book(self, book):
        if book.title in self.books:
            self.books[book.title].total_copies += book.total_copies 
            self.books[book.title].available_copies += book.total_copies
        else:
            self.books[book.title] = book 

    def borrow_book(self, title):
        if title in self.books and self.books[title].borrow_book():
            return f"You have successfully borrowed '{title}'."
        return f"Sorry, '{title}' is not available."
    
    def return_book(self, title):
        if title in self.books:
            self.books[title].return_book()
            return f"'{title}' has been returned."
        return f"'{title}' is not in our library records."
    
    def display_books(self):
        if not self.books:
            return "No books in the library."
        return "\n".join(str(book) for book in self.books.values()) 
    

class Member:
    def __init__(self, name):
        self.name = name 
        self.borrowed_books = []

    def borrow_book(self, library, title):
        message = library.borrow_book(title)
        if "successfully borrowed" in message:
            self.borrowed_books.append(title)
        return message
    
    def return_book(self, library, title):
        if title in self.borrowed_books:
            self.borrowed_books.remove(title)
            return library.return_book(title)
        return f"You haven't borrowed '{title}'."
    
    def __str__(self):
        return f"{self.name} (Borrowed books: {', '.join(self.borrowed_books) if self.borrowed_books else 'None'})"


# Example usage (correctly placed outside of the class)
library = Library()

book1 = Book("Python Programming", "John Doe", 3)
book2 = Book("Data Science Basics", "Jane Smith", 2)

library.add_book(book1)
library.add_book(book2)

# Creating a member
member1 = Member("Alice")

# Borrowing and returning books
print(member1.borrow_book(library, "Python Programming"))  # Successful
print(member1.borrow_book(library, "Python Programming"))  # Successful
print(member1.borrow_book(library, "Python Programming"))  # Successful
print(member1.borrow_book(library, "Python Programming"))  # Not available

print(member1.return_book(library, "Python Programming"))  # Successful return
print(member1.return_book(library, "Java Programming"))  # Book not borrowed

# Display books in the library
print("\nLibrary Books:")
print(library.display_books())

# Display member details
print("\nMember Info:")
print(member1)

