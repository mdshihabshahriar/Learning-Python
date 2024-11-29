class Book:
    def __init__(self,name,id,type,quantity):
        self.name = name
        self.id = id
        self.type = type
        self.quantity = quantity

class User:
    def __init__(self,name,id,password):
        self.name  = name
        self.id = id
        self.password = password
        self.borrowedBooks = []
        
class Library:
    def __init__(self,name,owner) -> None:
        self.name = name
        self.owner = owner
        self.books = []
        self.users = []
    
    def addBook(self,name,id,cat,quantity):
        book = Book(name,id,cat,quantity)
        self.books.append(book)
        print(f"\n\t<------ {book.name} Book added ------>")
    
    def addUser(self,id,name,password):
        user = User(name,id,password)
        self.users.append(user)
        return User 
    
    def borrowBook(self,user,id):
        for book in self.books:
            if book.id == id:
                if book in user.borrowedBooks:
                    print("\n\tAlready Borrowed!!!")
                    return
                elif book.quantity < 1:
                    print("\n\tNot Available!!!")
                    return
                else:
                    user.borrowedBooks.append(book)
                    book.quantity -= 1
                    print(f'\n\t{book.name} borrowed successfully!!')
                    return
        print('\n\tBook not found in borrowed list!!!!!')
        
    def returnBook(self,user,id):
        for book in user.borrowedBooks:
            if book.id == id:
                user.borrowedBooks.remove(book)
                book.quantity += 1
                print(f"\n\t{book.name} returned succesfully!!")
                return
        print("\n\tBook not found in borrowed list!!!")
        
    def showUsers(self):
        print(f"<------ User in the library ------->")
        for user in self.users:
            print(f"\n\tName: {user.name}, ID: {user.id}") 
    
    def showBooks(self):
        print("\n\t<----- Books in the Library ------->")
        for book in self.books:
            print(f"\n\tName: {book.name}, ID: {book.id}, Type: {book.type}, Quantity: {book.quantity}")
        
    def showBorrowedBooks(self, user):
        print("\n\t<----- Borrowed Books ------->")
        if user.borrowedBooks:
            for book in user.borrowedBooks:
                print(f"\n\tName: {book.name}, ID: {book.id}")
        else:
            print("\n\tNo books borrowed by this user.")   
    
    def showReturnedBooks(self, user):
        print("\n\t<----- Returned Books ------->")
        returned_books = [book for book in self.books if book not in user.borrowedBooks]
        if returned_books:
            for book in returned_books:
                print(f"\n\tName: {book.name}, ID: {book.id}")
        else:
            print("\n\tNo books returned by this user.") 
        
        
pl = Library('Shihab','Shahriar')
admin = pl.addUser(1,'Rakib',123)
sakib = pl.addUser(2,'Sakib',1234)
pb = pl.addBook('Dune',1,'Sci-Fic',5)
                   
        
currentUser='admin'

while True: 
    if currentUser == None:
        print(f'........No logged user!!!!..........')

        option = input("Login Or Register (L/R): ")

        if option == 'R':
            id = int(input("\tEnter id: "))
            name = input("\tEnter name: ")
            password = input("\tEnter password: ")

            user = pl.addUser(id, name, password)
            currentUser = user
        elif option == "L":
            id = int(input("\tEnter id: "))
            password = input("\tEnter password: ")
            match = False
            for user in pl.users:
                if user.id == id and user.password == password:
                    currentUser = user
                    match = True
                    break

            if match == False:
                print(f"\n\tUser Not found !")
    else:
        if currentUser == 'admin':
            print("Options\n")
            print("1 :Add Books")
            print("2 :Show Users")
            print("3 :Show Books")
            print("4 :Logout")

            ch = int(input("\nEnter Options: "))

            if ch == 1:
                cat = input("\tEnter cat: ")
                id = int(input("\tEnter id: "))
                name = input("\tEnter Name: ")
                quantity = int(input("\tEnter Quantity: "))
                pl.addBook(name, id, cat, quantity)  
            elif ch == 2:  
                pl.showUsers()
            elif ch == 3:
                pl.showBooks()
            elif ch == 4:  
                currentUser = None
                print("<-----\tLogged out successfully!------->")
                
        

        else:
            print("Options\n")
            print("1 :Borrow Books")
            print("2 :Return Books")
            print("3 :Show Books")
            print("4 :Show Borrowed Books")
            print("5 :Show Returned Books")
            print("6 :Logout")
            ch = int(input("\nEnter Options: "))

            if ch == 1:
                id = int(input("\tEnter id: "))
                pl.borrowBook(currentUser, id)
            elif ch == 2:
                id = int(input("\tEnter id: "))
                pl.returnBook(currentUser, id)
            elif ch == 3:
                pl.showBooks()
            elif ch == 4:
                pl.showBorrowedBooks(currentUser)
            elif ch == 5:
                pl.showReturnedBooks(currentUser)
            elif ch == 6:
                currentUser = None
                print("\n\tLogged out successfully!")    