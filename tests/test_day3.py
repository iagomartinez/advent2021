import unittest
from pathlib import Path
import context
from advent2021 import day3
THIS_DIR = Path(__file__).parent

class Tests(unittest.TestCase):
    def test_dayn(self):
        print('test_day3 tests')

        file = THIS_DIR.parent / 'data/day3_sample.txt'
        rows = day3.readbits(file)
        self.assertEqual(12, len(rows))
    
    def test_positioncounters(self):
        file = THIS_DIR.parent / 'data/day3_sample.txt'
        report = day3.readbits(file)
        print(report)

        counters = day3.countbits(report)
        gamma, epsilon = day3.computerates(counters)

        self.assertEqual(22, gamma)
        self.assertEqual(9, epsilon)