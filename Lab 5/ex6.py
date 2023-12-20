class LibraryItem:
    def __init__(self, title, item_id, checked_out=False):
        self.title = title
        self.item_id = item_id
        self.checked_out = checked_out

    def display_info(self):
        print(f"Item ID: {self.item_id}, Title: {self.title}, Checked Out: {self.checked_out}")

    def check_out(self):
        if not self.checked_out:
            print(f"{self.title} has been checked out.")
            self.checked_out = True
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        if self.checked_out:
            print(f"{self.title} has been returned.")
            self.checked_out = False
        else:
            print(f"{self.title} is not checked out.")

class Book(LibraryItem):
    def __init__(self, title, item_id, author, num_pages, checked_out=False):
        super().__init__(title, item_id, checked_out)
        self.author = author
        self.num_pages = num_pages

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}, Number of Pages: {self.num_pages}")

class DVD(LibraryItem):
    def __init__(self, title, item_id, director, running_time, checked_out=False):
        super().__init__(title, item_id, checked_out)
        self.director = director
        self.running_time = running_time

    def display_info(self):
        super().display_info()
        print(f"Director: {self.director}, Running Time: {self.running_time} minutes")

class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number, checked_out=False):
        super().__init__(title, item_id, checked_out)
        self.issue_number = issue_number

    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.issue_number}")

book = Book("The Great Gatsby", "B001", "F. Scott Fitzgerald", 180)
book.display_info()
book.check_out()
book.return_item()

dvd = DVD("Inception", "D001", "Christopher Nolan", 148)
dvd.display_info()
dvd.check_out()

magazine = Magazine("National Geographic", "M001", 256)
magazine.display_info()
magazine.return_item()
