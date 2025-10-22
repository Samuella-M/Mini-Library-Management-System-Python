"""
operations.py
Core logic for the Library Operations System (standalone version).
Implements book and member management using dictionaries, tuples, and lists.
"""

books = []
members = []
borrow_records = []

def add_book(isbn, title, author, category):
    """Add a book to the system if ISBN is unique."""
    for b in books:
        if b['isbn'] == isbn:
            return False
    books.append({'isbn': isbn, 'title': title, 'author': author, 'category': category, 'available': True})
    return True

def add_member(member_id, name, email):
    """Add a new member to the system."""
    for m in members:
        if m['id'] == member_id:
            return False
    members.append({'id': member_id, 'name': name, 'email': email})
    return True

def borrow_book(member_id, isbn):
    """Borrow a book if available."""
    book = next((b for b in books if b['isbn'] == isbn), None)
    member = next((m for m in members if m['id'] == member_id), None)
    if not book or not member or not book['available']:
        return False
    book['available'] = False
    borrow_records.append((member_id, isbn))
    return True

def return_book(member_id, isbn):
    """Return a borrowed book."""
    if (member_id, isbn) not in borrow_records:
        return False
    borrow_records.remove((member_id, isbn))
    for b in books:
        if b['isbn'] == isbn:
            b['available'] = True
    return True

def delete_book(isbn):
    """Delete a book only if not borrowed."""
    for b in books:
        if b['isbn'] == isbn:
            if not b['available']:
                return False
            books.remove(b)
            return True
    return False

def delete_member(member_id):
    """Delete member only if they have no borrowed books."""
    for record in borrow_records:
        if record[0] == member_id:
            return False
    for m in members:
        if m['id'] == member_id:
            members.remove(m)
            return True
    return False

def list_books():
    """Return list of all books."""
    return books

def list_members():
    """Return list of all members."""
    return members

def clear_data():
    books.clear()
    members.clear()
    borrow_records.clear()
