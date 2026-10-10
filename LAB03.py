class Book:
    def __init__(self):
        self.book_id = ""
        self.book_title = ""
        self.book_publisher = ""
        self.year_of_publication = ""

    def add_book(self):
        self.book_id = input("Enter book ID: ")
        self.book_title = input("Enter book title: ")
        self.book_publisher = input("Enter book publisher: ")
        self.year_of_publication = input("Enter book year of publication: ")

    def display_book(self):
        print("ID " + self.book_id)
        print("Title: " + self.book_title)
        print("Publisher: " + self.book_publisher)
        print("Year of publication: " + self.year_of_publication)

class Author:
    def __init__(self):
        self.author_id = ""
        self.author_afiliation = ""
        self.author_country = ""
        self.author_phone = ""
        self.author_email = ""
    def add_author(self):
        self.author_id = input("Enter author ID: ")
        self.author_afiliation = input("Enter author afiliation: ")
        self.author_country = input("Enter author country: ")
        self.author_phone = input("Enter author phone: ")
        self.author_email = input("Enter author email: ")
    def display_author(self):
        print("Author ID: " + self.author_id)
        print("Author Afiliation: " + self.author_afiliation)
        print("Author Country: " + self.author_country)
        print("Author Phone: " + self.author_phone)
        print("Author Email: " + self.author_email)
    def assign_book(self, book_id):
        self.book_id = book_id
class User:
    def __init__(self):
        self.user_id = ""
        self.user_name = ""
        self.user_password = ""
        self.user_address = ""
        self.user_phone = ""
        self.user_email = ""
        self.books_borrowed = 0
    def add_user(self):
        self.user_id = input("Enter user ID: ")
        self.user_name = input("Enter user name: ")
        self.user_password = input("Enter user password: ")
        self.user_address = input("Enter user address: ")
        self.user_phone = input("Enter user phone: ")
        self.user_email = input("Enter user email: ")
    def checkout_book(self, book_id):
        self.book_id = book_id
        self.books_borrowed = self.books_borrowed + 1
    def display_user(self):
        print("User ID: " + self.user_id)
        print("User Name: " + self.user_name)
        print("User Password: " + self.user_password)
        print("User Address: " + self.user_address)
        print("User Phone: " + self.user_phone)
        print("User Email: " + self.user_email)
        print("Books Borrowed: ", self.books_borrowed)
#Main Code
myBooklist = []
myAuthorlist = []
myUserlist = []

while True:
    print("1.Add Book")
    print("2.Add Author")
    print("3.Add User")
    print("4.Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        Book = Book()
        Book.add_book()
        myBooklist.append(Book)
        Book.display_book()
    elif choice == "2":
        Author = Author()
        Author.add_author()
        book_id = input("Enter book ID that this author wrote: ")
        Author.assign_book(book_id)
        myAuthorlist.append(Author)
        Author.display_author()
    elif choice == "3":
        User = User()
        User.add_user()
        book_id = int(input("Enter book ID of the book you wish to check out: "))
        User.checkout_book(book_id)
        myUserlist.append(User)
        User.display_user()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid input")