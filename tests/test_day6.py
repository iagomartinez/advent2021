import sys
import unittest
import time
from pathlib import Path
THIS_DIR = Path(__file__).parent
import context
from advent2021 import day6

class Tests(unittest.TestCase):

    def test_simplesimulate(self):        
        fish = day6.simulate(18, [3,4,3,1,2])
        self.assertEqual(26, len(fish))

    def test_fishindex(self):
        startingpoints = [3,4,3,1,2]
        fish = day6.buildfishindex(startingpoints)

        self.assertCountEqual([1,2,3,4], fish.keys())
        self.assertEqual(2, fish[3])

    def test_fastsimulation(self):
        startingpoints = [3,4,3,1,2]        
        fishindex = day6.faster_simulate(18, startingpoints)
        print(fishindex)
        self.assertEqual(26, sum(fishindex.values()))

    def test_fastsim_withbigggergen(self):        
        fishindex = day6.faster_simulate(256, [3,4,3,1,2])
        self.assertEqual(26984457539, sum(fishindex.values()))
