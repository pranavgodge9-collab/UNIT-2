class Library:
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
        self.is_available = True

    def check_out(self):
        if self.is_available:
            self.is_available = False
            print(f"You checked out '{self.book_name}'")
        else:
            print("Book is already checked out.")

    def return_book(self):
        self.is_available = True
        print(f"'{self.book_name}' returned.")

    def display_status(self):
        status = "Available" if self.is_available else "Checked Out"
        print(f"Book: {self.book_name} | Author: {self.author} | Status: {status}")

b1 = Library("The Great Gatsby", "F. Scott Fitzgerald")
b1.display_status()
b1.check_out()
b1.display_status()
