from unittest import TestCase
import comics_goodreads_ratings


class Test(TestCase):
    def test_read_books(self):
        books = comics_goodreads_ratings.read_books('./comixology_books_example.json')
        first_asin = books['objects'][0]['asin']
        self.assertEqual('B00AAJQVBS', first_asin)
