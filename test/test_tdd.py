import unittest


class TestSum(unittest.TestCase):
    """ Checking the various sum of the numbers."""

    def test_sum_list(self):
        """defining the condition to pass the list method. """
        self.assertEqual(sum([3, 4, 5]), 12, 'Should be 12.')

    def test_sum_tuple(self):
        """ defining the condition to fail the tuple method."""
        self.assertEqual(sum((2, 3, 6)), 12, 'Should be 12 as well')

    def test_sum_str(self):
        """ defining the condition to fail the mixed method."""
        values = ['True', '1', 2]
        self.assertEqual(sum([values]), 4, 'Should be 4 only.')

    def test_sum_negative(self):
        """ defining the condition to fail the mixed method."""

        self.assertEqual(sum([-1, 5]), 4, 'Should be 4 only.')



if __name__ == '__main__':
    unittest.main()
