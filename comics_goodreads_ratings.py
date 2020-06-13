import config
import json
import urllib.parse
import requests
import xml.etree.ElementTree as ET

GOODREADS_SEARCH_URL = 'https://www.goodreads.com/search.xml'


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
    with open(file_path) as json_file:
        return json.load(json_file)['objects']


def display_ratings(books):
    pass


def main():
    books = read_books('./comixology_books.json')
    for book in books:
        xml_book = search_goodreads_book(book)
        rating = fetch_book_rating(xml_book)
        keyword = get_goodreads_keyword(book)
        print(f'{keyword}: {rating}')


if __name__ == "__main__":
    main()
