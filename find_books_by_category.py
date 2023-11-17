import json

def find_books_by_category(category, books_data):
    filtered_books = [book for book in books_data if category.lower() in [c.lower() for c in book.get('categories', [])]]
    return filtered_books

def main():
    with open('books.json', 'r') as file:
        books_data = json.load(file)

    category = input("Enter category: ")

    books_in_category = find_books_by_category(category, books_data)
    
    for book in books_in_category:
        print(f"ISBN: {book['isbn']}, title: {book['title']}")

if __name__ == "__main__":
    main()
