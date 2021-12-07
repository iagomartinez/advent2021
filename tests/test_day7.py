import sys
import unittest
from pathlib import Path
import context
from collections import Counter
from functools import reduce
import time
from advent2021 import day7
THIS_DIR = Path(__file__).parent

class Tests(unittest.TestCase):
    def test_approaches(self):
        def scanall(input):
            cnt = Counter(input)
            print(cnt)
            totals = []
            for c1 in range(min(cnt), max(cnt)+1):
                totals.append(reduce((lambda tot, next: tot if next == c1 else tot+abs(next-c1)*cnt[next]), cnt,0))
            return totals
        
        for input in [([1,10,12]), ([1,2,3,4,5,6,7,8,9,10]), ([1,2,3,8,9,10])]:
            with self.subTest(msg=f'Testing {input}:', input=input):
                totals1 = scanall(input)
                totals2 = day7.crabfuel(input)
                self.assertEqual(min(totals1), min(totals2))

    def test_burnrate(self):
        inputs = [(5,16,66),(1,5,10),(2,5,6),(0,5,15),(4,5,1),(2,5,6),(7,5,3),(1,5,10),(2,5,6),(14,5,45)]
        for start, to, burn in inputs:
            with self.subTest(msg=f'Fuel burn test start:{start}, to:{to}:'):
                self.assertEqual(burn, day7.incrementalburn(0,start,to,1))

    def test_incrementalburn(self):
        input = 16,1,2,0,4,2,7,1,2,14
        totals = day7.crabfuel(input,burncalc=day7.incrementalburn)
        print(totals)
        self.assertEqual(168, min(totals))
