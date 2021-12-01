import unittest
from context import day1

class TestDay1(unittest.TestCase):
    def test_day1(self):
        depths = day1.readdepths('../data/day1_sample.txt')            
        self.assertEqual(10, len(depths))

    def test_countdepthincreases(self):
        depths = [199, 200]
        self.assertEqual(1, day1.countdepthincreases(depths))
        
    def test_sampledepths(self):
        depths = day1.readdepths('../data/day1_sample.txt')            
        self.assertEqual(7, day1.countdepthincreases(depths))