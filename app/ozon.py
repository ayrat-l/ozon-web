def create_book(title, author, price, tags, availability):
    return {
        'title': title,
        'author': author,
        'price': price,
        'tags': tags,
        'availability': availability,

    }

def add_book(container, book):
    copy = container[:]
    copy.append(book)
    return copy

def search_book_by_title(container, title):
    search_title = title.strip().lower()
    result = []
    for book in container:
        if search_title in book['title'].lower() == title.lower():
            result.append(book)
    return result



