import sys
import unittest
from pathlib import Path
THIS_DIR = Path(__file__).parent
import context
from advent2021 import day8
from functools import reduce

class Tests(unittest.TestCase):
    def test_dayn(self):
        print('test_day8 tests')
        

        testdata = [('be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',['fdgacbe', 'cefdb', 'cefbgd', 'gcbe'])]
        for input, outputs in testdata:
            with self.subTest(msg=f'parse pattern {input}:'):
                self.assertEqual(outputs, day8.parsepattern(input))

    def test_countdigits(self):
        file = THIS_DIR.parent / 'data/day8_sample.txt'
        with open(file, 'r', newline='', encoding='utf-8') as f:
            all_patterns = [pattern for line in f for pattern in day8.parsepattern(line.rstrip())]

        digitcounts = {2,4,3,7}
        targetdigits = reduce(lambda tot,nextp: tot + 1 if nextp in digitcounts else tot, list(map(lambda p: len(p), all_patterns)),0)
        self.assertEqual(26, targetdigits)


