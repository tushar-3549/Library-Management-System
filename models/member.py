class Member:
    def __init__(self, name, email):
        self.name = name 
        self. email =  email
    
    def save_to_db(self, db):
        db.execute_query("INSERT INTO members (name, email) VALUES (?, ?)", (self.name, self.email))

    @staticmethod
    def get_all_members(db):
        return db.fetch_all("SELECT * FROM members")