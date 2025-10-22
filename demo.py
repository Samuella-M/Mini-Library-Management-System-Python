"""
demo.py
Runs a demonstration of the Library Operations System.
"""

import operations

def run_demo():
    operations.clear_data()
    print("=== Library Operations System Demo ===")

    # Add sample books
    operations.add_book("001", "The Great Gatsby", "F. Scott Fitzgerald", "Fiction")
    operations.add_book("002", "Dune", "Frank Herbert", "Sci-Fi")
    operations.add_book("003", "A Brief History of Time", "Stephen Hawking", "Non-Fiction")

    # Add sample members
    operations.add_member(1, "Alice", "alice@mail.com")
    operations.add_member(2, "Bob", "bob@mail.com")

    print("\n-- Borrowing a Book --")
    print("Alice borrows 'The Great Gatsby':", operations.borrow_book(1, "001"))

    print("\n-- Attempt to Borrow Same Book --")
    print("Bob tries to borrow 'The Great Gatsby':", operations.borrow_book(2, "001"))

    print("\n-- Returning a Book --")
    print("Alice returns 'The Great Gatsby':", operations.return_book(1, "001"))

    print("\n-- Deleting a Member --")
    print("Deleting Bob:", operations.delete_member(2))

    print("\n-- Final Books --")
    for b in operations.list_books():
        print(b)

if __name__ == "__main__":
    run_demo()
