import sys
import unittest
from context import day2
from pathlib import Path
from functools import reduce

THIS_DIR = Path(__file__).parent

class Tests(unittest.TestCase):
    def test_readlines(self):
        print('test_day2 tests')
        input = day2.readlines(THIS_DIR.parent / 'data/day2_sample.txt')
        expected = [(5,0), (0,5), (8,0), (0,-3), (0,8), (2,0)]
        self.assertCountEqual(expected, input)

    def test_simpleposition(self):
        input = day2.readlines(THIS_DIR.parent / 'data/day2_sample.txt')
        pos,depth = day2.simpleposition(input)
        self.assertEqual(150, pos * depth)

    def test_positionwithaim(self):
        input = day2.readlines(THIS_DIR.parent / 'data/day2_sample.txt')
        pos,depth = day2.positionwithaim(input)
        
        self.assertEqual(15, pos)
        self.assertEqual(60, depth)
        self.assertEqual(900, pos * depth)
