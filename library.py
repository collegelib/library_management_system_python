# library.py

FILE_NAME = "books.txt"


def add_book(book_name, author):
    with open(FILE_NAME, "a") as file:
        file.write(f"{book_name},{author},Available\n")
    print("✅ Book added successfully.")


def view_books():
    try:
        with open(FILE_NAME, "r") as file:
            books = file.readlines()

        if not books:
            print("📂 No books available.")
            return

        print("\n--- Library Books ---")
        for index, book in enumerate(books, start=1):
            name, author, status = book.strip().split(",")
            print(f"{index}. {name} | {author} | {status}")

    except FileNotFoundError:
        print("📂 No books available.")


def issue_book(book_number):
    with open(FILE_NAME, "r") as file:
        books = file.readlines()

    if book_number < 1 or book_number > len(books):
        print("❌ Invalid book number.")
        return

    book_data = books[book_number - 1].strip().split(",")

    if book_data[2] == "Issued":
        print("⚠️ Book already issued.")
        return

    book_data[2] = "Issued"
    books[book_number - 1] = ",".join(book_data) + "\n"

    with open(FILE_NAME, "w") as file:
        file.writelines(books)

    print("📕 Book issued successfully.")


def return_book(book_number):
    with open(FILE_NAME, "r") as file:
        books = file.readlines()

    if book_number < 1 or book_number > len(books):
        print("❌ Invalid book number.")
        return

    book_data = books[book_number - 1].strip().split(",")

    if book_data[2] == "Available":
        print("⚠️ Book is already available.")
        return

    book_data[2] = "Available"
    books[book_number - 1] = ",".join(book_data) + "\n"

    with open(FILE_NAME, "w") as file:
        file.writelines(books)

    print("📗 Book returned successfully.")

