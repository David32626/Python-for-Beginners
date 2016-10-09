import sys
import unittest
from orderedlist import OrderedList

class OrderedListTest(unittest.TestCase):

    def setUp(self):
        self.mylist = OrderedList()

    def tearDown(self):
        self.mylist = None

    def test_size(self):
        self.mylist.add(31)
        self.mylist.add(77)
        self.mylist.add(17)
        self.mylist.add(93)
        self.mylist.add(26)
        self.mylist.add(54)
        self.assertEqual(self.mylist.size(), 6)

    def test_search(self):
        self.mylist.add(31)
        self.mylist.add(77)
        self.mylist.add(17)
        self.mylist.add(93)
        self.mylist.add(26)
        self.mylist.add(54)
        self.assertEqual(self.mylist.search(93), True)

    def test_find_list_item(self):
        self.mylist.add(31)
        self.mylist.add(77)
        self.mylist.add(17)
        self.mylist.add(93)
        self.mylist.add(26)
        self.mylist.add(54)
        self.assertEqual(self.mylist.find_list_item(), [17, 26, 31, 54, 77, 93])

if __name__ == '__main__':
    unittest.main()