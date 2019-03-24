import os

import waitress
from flask import Flask, render_template, request, url_for, redirect

from app.ozon import create_book, add_book, search_book_by_title, search_book_by_id, remove_book_by_id, \
    create_empty_book


def start():

    app = Flask(__name__)

    container = []
    wp = create_book('Война и Мир', 'Лев Толстой', 500, True, ['#война', '#любовь', '#толстой'])
    anna = create_book('Анна Каренина', 'Лев Толстой', 400, False, ['#поезд', '#любовь', '#толстой'])
    palata6 = create_book('Палата №6', 'Антон Чехов', 600, True, ['#больница', '#шесть', '#доктор'])

    #TODO: сделать распаковку в add_book

    container = add_book(container, wp)
    container = add_book(container, anna)
    container = add_book(container, palata6)

    @app.route('/')
    def index():
        search = request.args.get('search')
        if search:
            result = search_book_by_title(container, search)
            return render_template('index.html', books=result, search=search)
        return render_template('index.html', books=container)

    @app.route('/books/<book_id>')
    def book_details(book_id):
        result = search_book_by_id(container, book_id)
        return render_template('book-details.html', book=result)

    @app.route('/books/<book_id>/edit')
    def book_edit(book_id):
        book = None
        if book_id == 'new':
            book = create_empty_book()
        else:
            book = search_book_by_id(container, book_id)
        return render_template('book-edit.html', book=book)

    @app.route('/books/<book_id>/save', methods=['POST'])
    def book_save(book_id):
        nonlocal container
        title = request.form['title']
        author = request.form['author']
        price = request.form['price']
        availability = request.form['availability']
        tags = request.form['tags']

        if book_id == 'new':
            book = create_book(title=title, author=author, price=price, availability=availability, tags=tags)
            container = add_book(container, book)
        else:
            book = search_book_by_id(container, book_id)
            pass # TODO: сохранить изменения
        return redirect(url_for('book_details', book_id=book['id']))

    @app.route('/books/<book_id>/remove', methods=['POST'])
    def book_remove(book_id):
        nonlocal container
        container = remove_book_by_id(container, book_id)
        return redirect(url_for('index'))

    if os.getenv('APP_ENV') == 'PROD' and os.getenv('PORT'):
        waitress.serve(app, port=os.getenv('PORT'))
    else:
        app.run(port=9876, debug=True)

if __name__ == '__main__':
    start()