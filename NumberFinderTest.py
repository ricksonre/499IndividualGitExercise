import unittest
import NumberFinder

class NumberFinderTest(unittest.TestCase):
    def test_NotFound(self):
        array = [ 1, 2, 3, 4, 5]
        self.assertFalse(NumberFinder.find(0,array))

    def test_FoundFirst(self):
        array = [ 1, 2, 3, 4, 5]
        self.assertTrue(NumberFinder.find(1,array))

    def test_FoundLast(self):
        array = [ 1, 2, 3, 4, 5]
        self.assertTrue(NumberFinder.find(5,array))

if __name__ == '__main__':
    unittest.main()