import sys
import context
from advent2021 import day4
import unittest
from pathlib import Path
import re
THIS_DIR = Path(__file__).parent

class Tests(unittest.TestCase):
    def test_readnumberorder(self):
        file = THIS_DIR.parent / 'data/day4_sample.txt'
        number_order,_ = day4.readnumbers(file)
        self.assertEqual(27, len(number_order))

    def test_numbersregex(self):
        line = '22 13 17 11  0'
        numbers = day4.readrow(line)
        self.assertCountEqual([22,13,17,11,0], numbers)

    def test_rowregexleadingzero(self):
        line = ' 8  2 23  4 24'
        numbers = day4.readrow(line)
        self.assertCountEqual([8,2,23,4,24], numbers)

    def test_readboards(self):
        file = THIS_DIR.parent / 'data/day4_sample.txt'
        _, boards = day4.readnumbers(file)
        self.assertEqual(3, len(boards.values()))
        self.assertCountEqual(boards[0][0],[22,13,17,11,0])

    def test_buildindex(self):
        file = THIS_DIR.parent / 'data/day4_sample.txt'
        number_order, boards = day4.readnumbers(file)
        print(boards)

        index = day4.buildindex(boards)
        self.assertEqual(3, len(index))

    def test_drawnumber(self):
        file = THIS_DIR.parent / 'data/day4_sample.txt'
        number_order, boards = day4.readnumbers(file)
        index = day4.buildindex(boards)
        last_draw, winning_board, score = day4.drawnumbers(number_order, index)
        self.assertEqual(24, last_draw)
        self.assertEqual(2, winning_board)
        self.assertEqual(4512, score)
