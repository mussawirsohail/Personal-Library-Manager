import json

class PersonalLibraryManager:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.library = self.load_library()
    
    def load_library(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def save_library(self):
        with open(self.filename, "w") as file:
            json.dump(self.library, file, indent=4)
    
    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the author: ")
        year = int(input("Enter the publication year: "))
        genre = input("Enter the genre: ")
        read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
        
        book = {"title": title, "author": author, "year": year, "genre": genre, "read": read_status}
        self.library.append(book)
        print("Book added successfully!")
        self.save_library()
    
    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        self.library = [book for book in self.library if book["title"].lower() != title.lower()]
        print("Book removed successfully!")
        self.save_library()
    
    def search_book(self):
        choice = input("Search by:\n1. Title\n2. Author\nEnter your choice: ")
        query = input("Enter your search term: ").strip().lower()
        
        results = [book for book in self.library if 
                   (choice == "1" and book["title"].lower() == query) or 
                   (choice == "2" and book["author"].lower() == query)]
        
        if results:
            print("Matching Books:")
            for book in results:
                print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
        else:
            print("No matching books found.")
    
    def display_books(self):
        if not self.library:
            print("Your library is empty.")
        else:
            print("Your Library:")
            for book in self.library:
                print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    
    def display_statistics(self):
        total_books = len(self.library)
        read_books = sum(1 for book in self.library if book["read"])
        percentage_read = (read_books / total_books * 100) if total_books else 0
        
        print(f"Total books: {total_books}")
        print(f"Percentage read: {percentage_read:.1f}%")
    
    def menu(self):
        while True:
            print("\nWelcome to your Personal Library Manager!")
            print("1. Add a book")
            print("2. Remove a book")
            print("3. Search for a book")
            print("4. Display all books")
            print("5. Display statistics")
            print("6. Exit")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.remove_book()
            elif choice == "3":
                self.search_book()
            elif choice == "4":
                self.display_books()
            elif choice == "5":
                self.display_statistics()
            elif choice == "6":
                self.save_library()
                print("Library saved to file. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = PersonalLibraryManager()
    manager.menu()
