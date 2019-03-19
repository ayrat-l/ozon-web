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



