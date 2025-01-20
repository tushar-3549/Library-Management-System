from datetime import datetime

class Library:
    def __init__(self, db):
        self.db = db

    def issue_book(self, member_id, book_id):
        issue_date = datetime.now().strftime("%Y-%m-%d")
        self.db.execute_query("""
                              INSERT INTO issued_books (member_id, book_id, issue_date)
                              VALUES (?, ?, ?)""", (member_id, book_id, issue_date))

        self.db.execute_query("UPDATE books SET available = false WHERE id = ?", (book_id,))

    def return_book(self, book_id):
        return_date = datetime.now().strftime("%Y-%m-%d")
        self.db.execute_query("""
                              UPDATE issued_books 
                              SET return_date = ? 
                              WHERE book_id = ? AND return_date IS NULL""", (return_date, book_id))
        
        self.db.execute_query("UPDATE books SET available = true WHERE id = ?", (book_id,))