import unittest
from Calculator import *


class MyTestCase(unittest.TestCase):
    def test_emptyStringAdd(self):
        self.assertEqual(Add(""), 0)

    def test_singleNumberAdd(self):
        self.assertEqual(Add("1"), 1)
        self.assertEqual(Add("2"), 2)
        self.assertEqual(Add("3"), 3)

    def test_twoNumberAdd(self):
        self.assertEqual(Add("1,2"), 3)

    def test_multipleNumbersAdd(self):
        self.assertEqual(Add("1,2,3,4,5"), 15)

    def test_endlinesignAdd(self):
        self.assertEqual(Add("1\n2,3"), 6)

    def test_wrongexpresions(self):
        with self.assertRaises(ValueError):
            Add("1y,2")


if __name__ == '__main__':
    unittest.main()
