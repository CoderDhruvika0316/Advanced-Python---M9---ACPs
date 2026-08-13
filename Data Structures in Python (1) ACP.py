books = ["Secret Kingdom", "Charlie and the Chocolate Factory", "Horrid Henry", "Matilda", "Percy Jackson and the Olympians", "Amelia Jane"]

print(f"New Books in the Library: {books}")
print(f"Number of New Books In the Library: {len(books)}")
print(f"First Book: {books[0]}")
print(f"Last Book: {books[-1]}")
print(f"Last Four Books: {books[2:]}")

books.append("The Famous Five")
print(f"\nNew Books in the Library after Adding One: {books}")
books.remove("Horrid Henry")
print(f"New Books in the Library after Removing One: {books}")
books.sort()
print(f"New Books in the Library after Sorting Alphabetically: {books}")
books.reverse()
print(f"New Books in the Library after Reversing: {books}")

librarian = {"Name" : "Ms. Clark", "Section" : "Fiction", "Phone Number" : "0978821064", "Experience" : 3}
print(f"\nLibrarian Profile: {librarian}")

print(f"\nName of Librarian: {librarian["Name"]}")

librarian["Experience"] = 5
librarian["Email"] = "anya.forger@edencollege.com"
librarian.pop("Section")

print(f"Updated Librarian Profile: {librarian}\n")

book_ids = [101, 102, 103, 104, 105, 106, 107]
book_names = ["Secret Kingdom", "Charlie and the Chocolate Factory", "Horrid Henry", "Matilda", "Percy Jackson and the Olympians", "Amelia Jane", "The Famous Five"]

book_directory = dict(zip(book_ids, book_names))

print("-" * 201)
print("LIBRARY REPORT")
print("-" * 201)
print(f"Available Books in Library: {books}")
print(f"Librarian Profile: {librarian}")
print(f"Books Directory: {book_directory}")
print("-" * 201)