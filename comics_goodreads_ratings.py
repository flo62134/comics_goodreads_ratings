import config
import json
import urllib.parse
import requests
import xml.etree.ElementTree as ET
import typing

GOODREADS_SEARCH_URL = 'https://www.goodreads.com/search.xml'
SANITIZEDTITLES = {'Mister Miracle (2017-2019)': 'Mister Miracle'}


def sanitize_keyword(keyword):
    if SANITIZEDTITLES.get(keyword) is not None:
        return SANITIZEDTITLES.get(keyword)
    else:
        return keyword


def get_goodreads_keyword(book):
    title = book['title']
    number = book['volumeNumber']
    volume_title = book['volumeTitle']

    if title and number and volume_title:
        keyword = f'{title} {volume_title}'
    elif title and number and not volume_title:
        keyword = f'{title} {number}'
    elif title and not number and volume_title:
        keyword = f'{title} {volume_title}'
    else:
        keyword = f'{title}'

    return sanitize_keyword(keyword)


def get_goodreads_search_url(book):
    keyword = get_goodreads_keyword(book)
    query = urllib.parse.quote(keyword)
    return f'{GOODREADS_SEARCH_URL}?key={config.GOODREADS_API_KEY}&q={query}'


def search_goodreads_book(book):
    url = get_goodreads_search_url(book)
    goodreads_book = requests.get(url)
    return goodreads_book.text


def fetch_book_rating(book_xml: str):
    tree = ET.fromstring(book_xml)
    return tree.find('search').find('results').find('work').find('average_rating').text


def read_books(file_path: str):
    with open(file_path, 'rt', encoding='utf-8') as json_file:
        return json.load(json_file)['objects']


def display_ratings(books: typing.List):
    books.sort(key=lambda x: x['rating'], reverse=True)

    for book in books:
        keyword = book['keyword']
        rating = book['rating']
        print(f'{keyword}: {rating}')


def get_progress_status(book, books: typing.List):
    steps = len(books)
    current_step = books.index(book) + 1

    return f'Book {current_step}/{steps}'


def main():
    books = read_books('./comixology_books.json')

    for book in books:
        print(get_progress_status(book, books))
        xml_book = search_goodreads_book(book)
        book['keyword'] = get_goodreads_keyword(book)

        try:
            book['rating'] = fetch_book_rating(xml_book)
        except AttributeError as error:
            print(f'Error with keyword: %s', book['keyword'])

    display_ratings(books)


if __name__ == "__main__":
    main()
