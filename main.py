from models.database import Database
from models.member import Member
from models.library import Library
from models.book import Book

def main():
    db = Database()
    library = Library(db)

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Show All Books")
        print("6. Search Book by Title")
        print("7. Exit")

        try:
            choice = int(input("Enter your Choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1:
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            book = Book(title, author)
            book.save_to_db(db)
            print("Book Added Successfully...")
        elif choice == 2:
            name = input("Enter member name: ")
            email = input("Enter member email: ")
            member = Member(name, email)
            member.save_to_db(db)
            print("Member Added Successfully...")
        elif choice == 3:
            member_id = int(input("Enter member ID: "))
            book_id = int(input("Enter book ID: "))
            library.issue_book(member_id, book_id)
            print("Book issued successfully!")
        elif choice == 4:
            book_id = int(input("Enter book ID: "))
            library.return_book(book_id)
            print("Book returned successfully!")
        elif choice == 5:
            books = Book.get_all_books(db)
            for book in books:
                print(book)
        elif choice == 6:
            title = input("Enter book title to search: ")
            books = Book.search_by_title(db, title)
            for book in books:
                print(book)
        elif choice == 7:
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
