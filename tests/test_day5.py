import sys
import unittest
from pathlib import Path
import context
from advent2021 import day5
THIS_DIR = Path(__file__).parent

class Tests(unittest.TestCase):
    def test_parsesegment(self):
        text = '0,9 -> 5,9'
        x0,y0,x1,y1 = day5.parsesegment(text)
        self.assertEqual((0,9), (x0,y0))
        self.assertEqual((5,9), (x1,y1))

        text = '520,836 -> 564,880'
        x0,y0,x1,y1 = day5.parsesegment(text)
        self.assertEqual((520,836), (x0,y0))
        self.assertEqual((564,880), (x1,y1))

    def test_parsefile(self):
        file = THIS_DIR.parent / 'data/day5_sample.txt'
        coordinates= day5.parsefile(file)
        self.assertEqual(10, len(coordinates))

    def test_selectlines(self):
        file = THIS_DIR.parent / 'data/day5_sample.txt'
        coordinates= day5.parsefile(file)
        horz, vert, _ = day5.selectlines(coordinates)
        self.assertCountEqual([(0, 9, 5, 9),(9, 4, 3, 4), (0, 9, 2, 9), (3, 4, 1, 4)], horz)
        self.assertCountEqual([(2, 2, 2, 1),(7, 0, 7, 4)], vert)

    def test_buildindex(self):
        file = THIS_DIR.parent / 'data/day5_sample.txt'    
        dangerpoints = day5.finddangerpoints(file)
        print(dangerpoints)
        self.assertEqual(5, len(dangerpoints))

    def test_includediagonals(self):
        file = THIS_DIR.parent / 'data/day5_sample.txt'    
        dangerpoints = day5.finddangerpoints(file, True)
        print(dangerpoints)
        self.assertEqual(12, len(dangerpoints))

    def test_calcdiagonal(self):
        coords = day5.calcdiagonal(1,1,3,3)
        self.assertCountEqual([(1,1),(2,2),(3,3)], coords)

        coords = day5.calcdiagonal(9,7,7,9)
        self.assertCountEqual([(9,7),(8,8),(7,9)], coords)