# -------------------
# Abstraction + Encapsulation
# -------------------

class LibraryItem:
    """Abstract representation of any library item (book, magazine, etc.)."""
    def __init__(self, title, author):
        self._title = title       # protected (encapsulation: don't access directly outside)
        self._author = author
        self._is_borrowed = False

    def borrow(self):
        """Borrow item if available."""
        if self._is_borrowed:
            return False
        self._is_borrowed = True
        return True

    def return_item(self):
        """Return the item back to library."""
        if self._is_borrowed:
            self._is_borrowed = False
            return True
        return False

    def __str__(self):
        status = "Borrowed" if self._is_borrowed else "Available"
        return f"'{self._title}' by {self._author} - {status}"


# -------------------
# Inheritance
# -------------------

class Book(LibraryItem):
    """Book inherits from LibraryItem"""
    def __init__(self, title, author, pages=0):
        super().__init__(title, author)
        self.pages = pages

    # Polymorphism: Overriding __str__ to add extra info
    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} (Book, {self.pages} pages)"


class Magazine(LibraryItem):
    """Magazine inherits from LibraryItem"""
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = issue_number

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} (Magazine, Issue {self.issue_number})"


# -------------------
# Encapsulation + Abstraction
# -------------------

class Person:
    """Base class for any person in the library system"""
    def __init__(self, name):
        self._name = name  # encapsulation
        

class Member(Person):
    """Library member who can borrow/return items"""
    def __init__(self, name):
        super().__init__(name)
        self._borrowed_items = []

    def borrow_item(self, item: LibraryItem):
        if item.borrow():
            self._borrowed_items.append(item)
            print(f"{self._name} borrowed '{item._title}'.")
        else:
            print(f"Sorry, '{item._title}' is already borrowed.")

    def return_item(self, item: LibraryItem):
        if item in self._borrowed_items and item.return_item():
            self._borrowed_items.remove(item)
            print(f"{self._name} returned '{item._title}'.")
        else:
            print(f"{self._name} did not borrow '{item._title}'.")

    def __str__(self):
        borrowed_titles = ', '.join([i._title for i in self._borrowed_items]) or "No items borrowed"
        return f"Member: {self._name}, Borrowed Items: {borrowed_titles}"


# -------------------
# Library Management (Aggregation)
# -------------------

class Library:
    def __init__(self):
        self._items = []   # aggregation: library "has" items
        self._members = [] # aggregation: library "has" members

    def add_item(self, item: LibraryItem):
        self._items.append(item)
        print(f"Added {item}")

    def add_member(self, member: Member):
        self._members.append(member)
        print(f"Added member: {member._name}")

    def list_items(self):
        for item in self._items:
            print(item)

    def list_members(self):
        for member in self._members:
            print(member)


# -------------------
# Example Usage
# -------------------

library = Library()

# Add items
book1 = Book("1984", "George Orwell", 328)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
mag1 = Magazine("National Geographic", "Various", 202)

library.add_item(book1)
library.add_item(book2)
library.add_item(mag1)

# Add members
member1 = Member("Alice")
member2 = Member("Bob")
library.add_member(member1)
library.add_member(member2)

# Borrowing logic
member1.borrow_item(book1)
member2.borrow_item(book1)   # should fail (already borrowed)
member1.return_item(book1)
member2.borrow_item(book1)   # now works

# List final states
library.list_members()
library.list_items()
