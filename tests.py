"""
tests.py
Automated tests for Library Operations System.
"""

import operations

def run_tests():
    print("=== Running Library Operations Tests ===")
    operations.clear_data()

    assert operations.add_book("100", "Test Book", "Tester", "Fiction")
    assert not operations.add_book("100", "Duplicate Book", "Tester", "Fiction")

    assert operations.add_member(10, "Alice", "alice@mail.com")
    assert not operations.add_member(10, "Alice Duplicate", "alice@mail.com")

    assert operations.borrow_book(10, "100")
    assert not operations.borrow_book(10, "100")  # already borrowed

    assert not operations.delete_book("100")  # can't delete borrowed
    assert operations.return_book(10, "100")
    assert operations.delete_book("100")

    print("All tests passed successfully!")

if __name__ == "__main__":
    run_tests()
