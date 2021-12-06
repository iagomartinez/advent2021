import sys
import unittest
from pathlib import Path
THIS_DIR = Path(__file__).parent
import context
from advent2021 import day6

class Tests(unittest.TestCase):

    def test_dayn(self):
        print('test_day6 tests')
        
        fish = day6.simulate(18, [3,4,3,1,2])
        self.assertEqual(26, len(fish))
