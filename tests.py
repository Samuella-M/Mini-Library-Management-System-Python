
"""
tests.py
Automated simple tests / usage examples (at least 5 tests).
Run: python tests.py
"""
from library import *
import library

def run_tests():
    clear_data()
    print("TEST 1: Add genres-valid book")
    assert add_book("ISBN001", "The Great Gatsby", "F. Scott Fitzgerald", "Fiction") == True
    assert add_book("ISBN002", "A Brief History of Time", "Stephen Hawking", "Non-Fiction") == True
    print("  OK")

    print("TEST 2: Prevent duplicate ISBN")
    assert add_book("ISBN001", "Duplicate Book", "Someone", "Fiction") == False
    print("  OK")

    print("TEST 3: Add members and prevent duplicate")
    assert add_member(101, "Alice", "alice@example.com") == True
    assert add_member(102, "Bob", "bob@example.com") == True
    assert add_member(101, "Alice2", "alice2@example.com") == False
    print("  OK")

    print("TEST 4: Borrow & return operations")
    assert borrow_book(101, "ISBN001") == True   # Alice borrows Gatsby
    assert borrow_book(102, "ISBN001") == False  # cannot borrow already borrowed book
    assert member_borrowed_books(101)[0]["isbn"] == "ISBN001"
    assert return_book(101, "ISBN001") == True
    assert return_book(101, "ISBN001") == False  # already returned
    print("  OK")

    print("TEST 5: Prevent deleting borrowed book / deleting member with borrowed books")
    # setup
    assert borrow_book(102, "ISBN002") == True
    assert delete_book("ISBN002") == False  # cannot delete borrowed
    assert delete_member(102) == False      # cannot delete member with borrowed books
    assert return_book(102, "ISBN002") == True
    assert delete_book("ISBN002") == True
    assert delete_member(102) == True
    print("  OK")

    print("All tests passed. Current books:", list_books())
    print("All tests completed successfully.")

if __name__ == "__main__":
    run_tests()
