import config
import json

GOODREADS_SEARCH_URL = 'https://www.goodreads.com/search.xml'


def get_book_query(book):
    pass


def search_book(book):
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
    print(books)


if __name__ == "__main__":
    main()
