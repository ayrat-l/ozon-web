import uuid


def create_book(title, author, price, availability, tags):
    return {
        'id': str(uuid.uuid4()),
        'title': title,
        'author': author,
        'price': price,
        'availability': availability,
        'tags': tags,
    }

def create_empty_book():
    return {
        'id': str(uuid.UUID()),
        'title': '',
        'author': '',
        'price': '',
        'availability': '',
        'tags': '',
    }

def add_book(container, book):
    copy = container[:]
    copy.append(book)
    return copy

def search_book_by_title(container, search):
    search_word = search.strip().lower()
    result = []
    for book in container:
        if search_word in book['title'].lower():
            result.append(book)
        if search_word in book['tags']:
            result.append(book)
        if search_word in book['author'].lower():
            result.append(book)
    return result


def search_book_by_id(container, book_id):
    for book in container:
        if book['id'] == book_id:
            return book

def remove_book_by_id(container, book_id):
    result = []
    for book in container:
        if book['id'] != book_id:
            result.append(book)
    return result
