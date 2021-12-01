import unittest
from context import day1

class TestDay1(unittest.TestCase):
    def test_day1(self):
        depths = day1.readdepths('../data/day1_sample.txt')            
        self.assertEqual(10, len(depths))

