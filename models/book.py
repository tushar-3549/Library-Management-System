class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def save_to_db(self, db):
        db.execute_query("INSERT INTO books (title, author) VALUES (?, ?)", (self.title, self.author))
    
    @staticmethod
    def get_all_books(db):
        return db.fetch_all("SELECT * FROM books")
    
    @staticmethod
    def search_by_title(db, title):
        search = db.fetch_all("SELECT * FROM books where title LIKE ?", (f"%{title}%",))
        return search