from flask import Flask, render_template, request

from app.ozon import create_book, add_book, search_book_by_title


def main():

    app = Flask(__name__)

    container = []
    wp = create_book('Война и Мир', 'Лев Толстой', 500, ['#война', '#любовь', '#толстой'], True)
    anna = create_book('Анна Каренина', 'Лев Толстой', 400, ['#война', '#любовь', '#толстой'], False)
    palata6 = create_book('Палата 6', 'Антон Чехов', 600, ['#больница', '#шесть', '#доктор'], True)

    #TODO: сделать распаковку в add_book

    container = add_book(container, wp)
    container = add_book(container, anna)
    container = add_book(container, palata6)

    @app.route('/')
    def index():
        search = request.args.get('search')
        if search:
            #TODO почистить, нижний регистр
            result = search_book_by_title(container, search)
            return render_template('index.html', books=result, search=search)
        return render_template('index.html', books=container)

    app.run(port=9876, debug=True)

if __name__ == '__main__':
    main()