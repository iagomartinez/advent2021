import sys
import unittest
from pathlib import Path
THIS_DIR = Path(__file__).parent
import re
import context
from advent2021 import day13

class Tests(unittest.TestCase):
    #   cases:
    #   1. fold point to the left of fold
    #   2. fold point to the right of fold
    #   3. fold point on the line
    #   4. fold, point is visible
    #   5. fold, point overlaps

    def test_fold_y(self):        
        input = '6,10'
        fold = 'fold along y=7'

        point = day13.parsepoint(input)
        self.assertEqual((6,10), point)

        foldline = day13.parsefold(fold)
        self.assertEqual((0,7), foldline)

        folded = day13.fold(point, foldline)
        self.assertEqual((6, 4), folded)

    def test_fold_x(self):
        input = '6,10'
        fold = 'fold along x=5'

        foldline = day13.parsefold(fold)
        self.assertEqual((5,0), foldline)

        folded = day13.fold(day13.parsepoint(input), foldline)
        self.assertEqual((4,10), folded)

    def test_fold_on_line(self):
        folded = day13.fold((6,10), day13.parsefold('fold along x=6'))
        self.assertIsNone(folded)

        folded = day13.fold((6,10), day13.parsefold('fold along y=10'))
        self.assertIsNone(folded)

    def test_parsefile(self):
        file = THIS_DIR.parent / 'data/day13_sample.txt'
        points, folds = day13.parsefile(file)
        self.assertEqual(18, len(points))
        self.assertEqual(2, len(folds))

    def test_foldpoints(self):
        points = {(6,10),(6,4)}
        fold = day13.parsefold('fold along y=7')

        folded = day13.foldpoints(points, fold)
        print(folded)   
        self.assertCountEqual({(6,4)}, folded)


