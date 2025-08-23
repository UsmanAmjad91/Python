# Base Class
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price:.2f}")


# Derived Class
class EBook(Book):
    def __init__(self, title, author, price, file_size):
        super().__init__(title, author, price)
        self.file_size = file_size  # in MB

    # Overriding display_details method (polymorphism)
    def display_details(self):
        super().display_details()
        print(f"File Size: {self.file_size} MB")


# Main code
if __name__ == "__main__":
    # Create Book objects
    book1 = Book("1984", "George Orwell", 9.99)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 12.50)

    # Create EBook object
    ebook1 = EBook("Digital Fortress", "Dan Brown", 5.99, 2.5)

    # Display details of all books
    print("=== Book 1 ===")
    book1.display_details()

    print("\n=== Book 2 ===")
    book2.display_details()

    print("\n=== E-Book ===")
    ebook1.display_details()
