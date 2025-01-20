import sqlite3

class Database:
    def __init__(self, db_name="db/library.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS books (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT NOT NULL,
                            author TEXT NOT NULL,
                            available BOOLEAN DEFAULT true
                            )
        """)

        self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS members (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            email TEXT NOT NULL UNIQUE
                            )
        """)

        self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS issued_books (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            member_id INTEGER,
                            book_id INTEGER,
                            issue_date TEXT,
                            return_date TEXT,
                            FOREIGN KEY (member_id) REFERENCES members (id),
                            FOREIGN KEY (book_id) REFERENCES books (id)
                            )
        """)

        self.connection.commit()

    def execute_query(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetch_all(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetch_one(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()
