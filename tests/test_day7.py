import unittest
from pathlib import Path
import context
from advent2021 import day7
THIS_DIR = Path(__file__).parent

class Tests(unittest.TestCase):
    def test_sipleburn(self):
        input = 16,1,2,0,4,2,7,1,2,14
        totals = day7.crabfuel(input)
        self.assertEqual(37, min(totals))

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
