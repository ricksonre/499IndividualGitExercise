import unittest
import ElementCounter

class ElementCounterTest(unittest.TestCase):
    def test_FoundZero(self):
        array = [ 1, 2, 3, 4, 5]
        self.assertFalse(ElementCounter.count(0,array))

    def test_FoundOne(self):
        array = [ 1, 2, 3, 4, 5]
        self.assertTrue(ElementCounter.count(1,array))

    def test_FoundThree(self):
        array = [ 1, 1, 1, 4, 5]
        self.assertTrue(ElementCounter.count(1,array))

if __name__ == '__main__':
    unittest.main()