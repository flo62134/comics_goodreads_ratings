from unittest import TestCase
import comics_goodreads_ratings


class Test(TestCase):
    def test_read_books(self):
        books = comics_goodreads_ratings.read_books('./comixology_books_example.json')
        first_asin = books['objects'][0]['asin']
        self.assertEqual('B00AAJQVBS', first_asin)

    def test_get_goodreads_keyword_no_volume_title(self):
        book = dict(title='Amazing Spider-Man Masterworks', volumeNumber="1", volumeTitle=None)

        actual = comics_goodreads_ratings.get_goodreads_keyword(book)
        expected = 'Amazing Spider-Man Masterworks 1'
        self.assertEqual(actual, expected)

    def test_get_goodreads_keyword_no_volume_info(self):
        book = dict(title='Amazing Spider-Man: Red Goblin', volumeNumber=None, volumeTitle=None)

        actual = comics_goodreads_ratings.get_goodreads_keyword(book)
        expected = 'Amazing Spider-Man: Red Goblin'
        self.assertEqual(actual, expected)

    def test_get_goodreads_keyword_all_info(self):
        book = dict(title="Avengers by Jason Aaron", volumeNumber="1", volumeTitle="The Final Host")

        actual = comics_goodreads_ratings.get_goodreads_keyword(book)
        expected = 'Avengers by Jason Aaron The Final Host'
        self.assertEqual(actual, expected)
