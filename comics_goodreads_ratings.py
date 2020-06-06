import config
import json

GOODREADS_SEARCH_URL = 'https://www.goodreads.com/search.xml'


def get_goodreads_query(book):
    pass


def get_goodreads_keyword(book):
    title = book['title']
    number = book['volumeNumber']
    volume_title = book['volumeTitle']

    if title and number and volume_title:
        return f'{title} {volume_title}'
    elif title and number and not volume_title:
        return f'{title} {number}'
    elif title and not number and volume_title:
        return f'{title} {volume_title}'
    else:
        return f'{title}'


def search_goodreads_book(book):
    pass


def fetch_book_rating(book: str):
    pass


def read_books(file_path: str):
    with open(file_path) as json_file:
        return json.load(json_file)


def display_ratings(books):
    pass


def main():
    books = read_books('./comixology_books.json')


if __name__ == "__main__":
    main()
