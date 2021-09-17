import unittest
import ElementCounter

class ElementCounterTest(unittest.TestCase):
    def test_FoundZero(self):
        array = [ 1, 2, 3, 4, 5]
        self.assertEqual(ElementCounter.count(0,array), 0)

    def test_FoundOne(self):
        array = [ 1, 2, 3, 4, 5]
        self.assertEqual(ElementCounter.count(1,array), 1)

    def test_FoundThree(self):
        array = [ 1, 1, 1, 4, 5]
        self.assertEqual(ElementCounter.count(1,array), 3)

if __name__ == '__main__':
    unittest.main()