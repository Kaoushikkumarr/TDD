import unittest
from unittest import TestCase

# from setuptools.extension import Library


class Library(object):
    def __init__(self):
        self.catalogue = []

    def donate(self, movie):
        self.catalogue.append(movie)


class DonateMovieTest(unittest.TestCase):   #Test Case for Donate Movie.

    def test_donate_movie(self):
        movie = Movie()
        library = Library()
        library.donate(movie)
        self.assertTrue(movie in Library.catalogue)




if __name__ == '__main__':
    unittest.main()
