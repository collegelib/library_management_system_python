# main.py

import library


def show_menu():
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")


while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter book name: ")
        author = input("Enter author name: ")
        library.add_book(name, author)

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        library.view_books()
        num = int(input("Enter book number to issue: "))
        library.issue_book(num)

    elif choice == "4":
        library.view_books()
        num = int(input("Enter book number to return: "))
        library.return_book(num)

    elif choice == "5":
        print("👋 Thank you for using the Library System.")
        break

    else:
        print("❌ Invalid choice. Try again.")

