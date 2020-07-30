''' Trying to driven into the Unit TestCases '''

import unittest
# from unittest import TestCase
# from setuptools.extension import Library


class Library:
    """ Initializing the variables """

    catalogue = None

    def __init__(self):
        self.catalogue = []

    def donate(self, movie):  # pylist: missing-function-docstring
        self.catalogue.append(movie)


class Movie:
    """ Creating movie class """
    STAT = 25

    def func(self):
        """ Passing the method """
        pass


class DonateMovieTest(unittest.TestCase):
    """ creating test class for movie """

    def test_donate_movie(self):  # created another function
        """ creating test class for movie """
        movie = Movie()
        library = Library()
        library.donate(movie)
        self.assertTrue(movie in Library.catalogue)


if __name__ == '__main__':
    unittest.main()
